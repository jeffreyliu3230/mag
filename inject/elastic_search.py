import logging
import settings
import sys

from elasticsearch import Elasticsearch, helpers
from celery import Celery
from ipyparallel import Client

logger = logging.getLogger(__name__)

try:
    es = Elasticsearch(settings.ELASTIC_URI, request_timeout=settings.ELASTIC_TIMEOUT, retry_on_timeout=True)

    es.cluster.health(wait_for_status='yellow')
    es.indices.create(index=settings.ELASTIC_INDEX, body={}, ignore=400)
except ConnectionError:
    logger.error('Could not connect to Elasticsearch, expect errors.')
    raise


def get_records(table_name, suffix='.txt', echo):
    size = 0
    with open(''.join([settings.MAG_PATH, table_name, suffix]), 'r') as f:
        for line in f:
            try:
                items = line.split('\t')
                if echo:
                    size += sys.getsizeof(line)
                    sys.stdout.write("\rimported {} MBs".format(round(float(size) / (10 ** 6), 2)))
                    sys.stdout.flush()
                yield items
            except KeyboardInterrupt:
                c = raw_input("quit(q) or continue(c): ")
                if c == "q":
                    quit()
                elif c == "c":
                    continue


def to_doc(fieldnames, record):
    # map keys and values in a dictionary
    return dict(zip(fieldnames, record))


def construct_action(action, doc_type, doc_id, doc):
    return {
        '_op_type': action,
        '_index': settings.ELASTIC_INDEX,
        '_type': doc_type,
        '_id': doc_id,
        'doc': doc,
        'upsert': doc
    }


def actions(action, table_name, echo):
    fieldnames = settings.FIELD_NAMES[table_name]
    for record in get_records(table_name, echo):
        # Do processing to records
        record = map(lambda x: x.strip(), record)
        doc_type = settings.TYPES[table_name]
        doc_id = '|'.join(record[0:settings.TABLE_IDs[table_name]])
        doc = to_doc(fieldnames, record)
        yield construct_action(action, doc_type, doc_id, doc)


def bulk_process(table_name, method, action='update', echo=False):
    if method == 'celery':
        app = Celery('elastic_search', broker='amqp://localhost')
        for acts in actions_wrapper(action, table_name, echo):
            async_bulk_wrapper.delay(acts)
    elif method == 'parallel':
        pass


@app.task(bind=True, default_retry_delay=30)
def async_bulk_wrapper(self, acts):
    try:
        return helpers.bulk(es, acts, stats_only=True)
    except Exception as e:
        logger.info(e)
        raise self.retry(exc=e)


def actions_wrapper(action, table_name, echo=True, size=500):
    count = 0
    acts = []
    for action in actions(action, table_name, echo):
        acts.append(action)
        count += 1
        if count == size:
            yield acts
            count = 0
            acts = []
if __name__ == '__main__':
    for i in get_records('Authors', True):
        print(i)
