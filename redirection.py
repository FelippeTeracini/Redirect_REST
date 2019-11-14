from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import requests
import json
app = FastAPI()

tasks_dictionary = {}
new_ip = 'http://101.193.193.10:5000'


class Task(BaseModel):
    title: str
    description: str
    done: bool


@app.get("/")
def read_root():
    return requests.get(new_ip + '/').json()


@app.get("/task")
def read_tasks():
    return requests.get(new_ip + '/task').json()


@app.post("/task")
def create_task(task: Task):
    return requests.post(new_ip + '/task',
                         data=json.dumps(task))


@app.get("/task/{task_id}")
def read_task(task_id: int):
    return requests.get(new_ip + '/task/' + task_id).json()


@app.put("/task/{task_id}")
def update_task(task_id: int, task: Task):
    return requests.post(new_ip + '/task/' + task_id,
                         data=json.dumps(task))


@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    return requests.delete(new_ip + '/task/' + task_id).json()


@app.get("/healthcheck")
def read_health():
    return requests.get(new_ip + '/healthcheck').json()
