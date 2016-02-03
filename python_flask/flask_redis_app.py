
from flask import Flask
from redis import Redis

import os
import socket

app = Flask(__name__)

redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def helloworld():
    redis.incr('page_visits')
    return '\nHello World!\nThis page has been visited %s times.\nOn host %s\n\n' % (redis.get('page_visits') ,host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

