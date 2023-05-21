from flask import Flask, request as req
import requests
from celery import Celery

app = Flask(__name__)
simple_app = Celery('simple_worker',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='rpc://')


@app.route('/send_data_to_1c', methods=['POST'])
def call_method():
    data = req.get_json()
    app.logger.info("Invoking Method ")
    r = simple_app.send_task('tasks.longtime_add', kwargs={"name": data['name'], "age": data['age']})
    app.logger.info(r.backend)
    return r.id


@app.route('/task_result/<task_id>')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


