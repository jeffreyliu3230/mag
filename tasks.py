import json
import time

from invoke import run, task


@task
def inject(table_name, method='celery'):
    from inject.elastic_search import bulk_process
    start_time = time.time()
    bulk_process(table_name, method, echo=True)
    stop_time = time.time()
    run_time = stop_time - start_time
    print("--run time: {}--".format(run_time))
    with open('runtime.txt', 'a') as f:
        f.write("{}(method: {}): {}\n".format(table_name, method, run_time))
