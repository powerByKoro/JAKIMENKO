from flask import Flask, request as req
import requests
import json
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='rpc://')

@app.task()
def longtime_add(name, age):
    headers = dict(Accept='application/json')
    dataPOST = {"Description": name, "Имя": name, "Возраст": age}
    # responce = requests.get('https://google.com')
    responcePOST = requests.post("https://004d-176-106-245-245.ngrok-free.app/baza/odata/standard.odata/Catalog_Студенты?$format=json",
                                 headers=headers,
                                 data=json.dumps(dataPOST))

    return responcePOST.json()
