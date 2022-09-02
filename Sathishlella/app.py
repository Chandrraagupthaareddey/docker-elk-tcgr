# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:50:12 2020

@author: Sathish
"""


from flask import Flask, render_template, Response
from camera import VideoCamera
app = Flask(__name__)
@app.route('/')
def home():
    # rendering webpage
    return render_template('home.html')

@app.route('/index')
def index():
    # rendering webpage
    return render_template('index.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(debug=True)
