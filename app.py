import redis
from flask import Flask, render_template, request

app = Flask(__name__)
db = redis.StrictRedis('localhost', 6379, 0)

@app.route('/')
def main():
    c = db.incr('user_count')
    return render_template('main.html', connected=c)
