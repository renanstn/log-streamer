import os
import time
from flask import Flask


app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong!"

@app.route("/log")
def stream_logs():
    FILE_PATH = os.getenv("FILE_PATH")
    if not FILE_PATH:
        raise Exception("Missing env variable 'FILE_PATH'.")
    with open(FILE_PATH, "r") as log_file:
        log_file.seek(0, os.SEEK_END)
        while True:
            last_line = log_file.readline()
            if not last_line:
                time.sleep(0.1)
                continue
            yield last_line
