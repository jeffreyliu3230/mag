# Working with Microsoft Academic Graph data

----
## Installation
    pip install -r requirements.txt
    brew install elasticsearch
    brew install rabbitmq

## Configuration
Under inject, change ELASTIC_URI and MAG\_PATH.



## Quick start
Launch RabbitMQ

    rabbitmq-server

Launch two celery workers

    celery worker -A inject.elastic_search --loglevel=info -n worker_1
    celery worker -A inject.elastic_search --loglevel=info -n worker_2

Launch elasticsearch

    elasticsearch

If you want to use the customized settings file provided, do

    elasticsearch -Des.config=/your-path/mag/elasticsearch_mag.yml

Or create an alias in your .bash_profile:

    alias elasticsearch_mag='elasticsearch -Des.config=/your-path/mag/elasticsearch\_mag.yml'

Then type in terminal:

    elasticsearch_mag

Inject data

    invoke inject <table_name>

By default it is using Celery. the method "parallel" is still under development.
