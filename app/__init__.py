# coding:utf-8

from flask import Flask
from flask import render_template
from flask import make_response
from flask import request

from lastfm import user_artists

import sys
import json
import socket
import time

app = Flask(__name__)
host = socket.gethostname()


def r_render(tmplt, env):
    return render_template(tmplt, env=env)


def get_artists(username):
    if not username or username == '':
        return []
    return user_artists(username)


@app.route("/")
@app.route("/people", methods=['GET', 'POST'])
def people():
    expr = request.args.get('expr')
    print expr
    env = {}
    return r_render('people.html', env)

if __name__ == "__main__":
    app.run()
