import settings
import sys

from elasticsearch import Elasticsearch

es = Elasticsearch(ELASTIC_URI)

# import Field of Study
size = 0

with open(''.join([MAG_PATH, 'Conferences.txt']), 'r') as f:
    for line in f.readlines():
        items = line.split('\t')
        doc = {
            'field_of_study': items[1]
        }
        res = es.index(index=index, doc_type='conferences', id=items[0], body=doc)
        size += sys.getsizeof(line)
        sys.stdout.write("\rimported {} MBs".format(size))
        sys.stdout.flush()
