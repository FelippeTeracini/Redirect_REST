from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import requests
import sys
import getopt
import json

app = FastAPI()

server_address = ''
PORT = 0


class Task(BaseModel):
    title: str
    description: str
    done: bool


@app.get("/")
def read_root():
    return requests.get(server_address + '/').json()


@app.get("/task")
def read_tasks():
    return requests.get(server_address + '/task').json()


@app.post("/task")
def create_task(task: Task):
    return requests.post(server_address + '/task',
                         data=json.dumps(task))


@app.get("/task/{task_id}")
def read_task(task_id: int):
    return requests.get(server_address + '/task/' + task_id).json()


@app.put("/task/{task_id}")
def update_task(task_id: int, task: Task):
    return requests.post(server_address + '/task/' + task_id,
                         data=json.dumps(task))


@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    return requests.delete(server_address + '/task/' + task_id).json()


@app.get("/healthcheck")
def read_health():
    return requests.get(server_address + '/healthcheck').json()


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "h", ["server_address=", "port="])
    except getopt.GetoptError:
        print(
            'redirection.py --server_address <server-address> --port <port>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--server_address':
            server_address = arg
        elif opt == '--port':
            PORT = arg

    uvicorn.run("redirection:app", host=server_address,
                port=PORT, log_level="info")


if __name__ == "__main__":
    main(sys.argv[1:])
