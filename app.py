from flask import Flask, render_template, redirect, request
import interface
from save import *
from user_profile import *
from gradientDescent import MLBackend
app = Flask(__name__)
backend = MLBackend()
RoomPF = []

@app.route('/')
def main():
    return render_template('landing.html')

@app.route('/swipe')
def start():
    global RoomPF
    profile = interface.request_user_profile_from_backend()
    return render_template('index.html', name=profile.name, age=profile.age, location=profile.location, bio=profile.bio, pfimg=profile.profile_picture,
    gender=round(RoomPF[0], 4),
    smoke=round(RoomPF[1], 4),
    candle=round(RoomPF[2], 4),
    pet=round(RoomPF[3], 4),
    instrument=round(RoomPF[4], 4),
    clean=round(RoomPF[5], 4),
    cook=round(RoomPF[6], 4),
    friends=round(RoomPF[7], 4),
    wake=round(RoomPF[8], 4),
    sleep=round(RoomPF[9], 4),
    decorate=round(RoomPF[10], 4),
    noise=round(RoomPF[11], 4))
    
@app.route('/refresh')
def refresh():
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verify', methods=['POST'])
def verify():
    global RoomPF
    name = request.form['name']
    RoomPF = backend.getProfile()
    profile = load_user_profile(name)
    if profile == None:

        profile = user_profile()
        profile.name = name
        profile.age = 42
        profile.bio = "This is an interesting biography of a new user of this site"
        save_user_profile(name, profile)

    return redirect('/swipe')

@app.route('/like', methods = ['POST'])
def like():
    global RoomPF
    backend.dataLoad(RoomPF, 1)
    RoomPF = backend.getProfile()
    return redirect('/swipe')

@app.route('/dislike', methods = ['POST'])
def dislike():
    global RoomPF
    backend.dataLoad(RoomPF, 0)
    RoomPF = backend.getProfile()
    return redirect('/swipe')

if __name__ == '__main__':
    app.run()


