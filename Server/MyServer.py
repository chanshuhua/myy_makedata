import base64
import json
import os
import time
from random import random
import jwt
import flask
from flask import Flask, url_for
from flask import request
from flask import render_template
from flask_wtf.file import file_allowed,file_required,file_size


server = Flask(__name__,template_folder='D:\Workspaces\myy_makedata\Server')
server.config['UPLOAD_PATH'] = os.path.join(server.root_path, 'files')
users=[{"chenshuhua":111},{"chenshuhua":222}]
response = {"code":0,"message":None,"token":None}

def login_do_get():
    return render_template('login.html')

def login_do_post(data):
    message,code,token = None,0,None
    username = data.get("username")
    pwd = data.get("password")
    if username and pwd:
        for i in users:
            if username == list(i.keys())[0] and str(pwd) == str(list(i.values())[0]):
                message = "success login. hello %s! " %username
                code = 1
                break
            if username != list(i.keys())[0]:
                message = "incorrect username"
                code = -1
            if username == list(i.keys())[0] and str(pwd) != str(list(i.values())[0]):
                message = "incorrect password"
                code = -1
    else:
        message = "incorrect request!"
    if code == 1:
        # 假装一下的token
        token = base64.b64encode((":".join([str(username), str(random()), str(time.time()+7200)])).encode()).decode()
        response.update({"code":code,"message":message,"token":token})
    return response

def upload(f):

    f.save(os.path.join(server.config['UPLOAD_PATH'], f.filename))
    f.close()
    return "success"

@server.route("/login",methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if flask.request.form:
            data = flask.request.form.to_dict()
        if flask.request.data:
            data = json.loads(flask.request.data)
        if flask.request.files:
            f = flask.request.files.get('file')
            fd = upload(f)

        return login_do_post(data)

    if request.method == 'GET':
        # flask.render_template("login.html")
        return login_do_get()

    else:
        error = 'Invalid request!'
        return error
if __name__ == '__main__':
    server.run(host='localhost',port='59999',debug=True)
    # users = [{"chenshuhua": 111}, {"chenshuhua": 222}]
    # for i in users:
    #     print(list(i.values())[0])