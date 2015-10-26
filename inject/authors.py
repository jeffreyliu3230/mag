import settings
import sys

from elasticsearch import Elasticsearch

es = Elasticsearch(settings.ELASTIC_URI)

# import Field of Study
size = 0

with open(''.join([settings.MAG_PATH, 'Authors.txt']), 'r') as f:
    for line in f.readlines():
        items = line.split('\t')
        doc = {
            'author_name': items[1]
        }
        res = es.index(index=index, doc_type='authors', id=items[0], body=doc)
        size += sys.getsizeof(line)
        sys.stdout.write("\rimported {} MBs".format(size))
        sys.stdout.flush()
