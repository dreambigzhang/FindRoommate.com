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
    #smoke
    if RoomPF[1] > 0.5:
        smoke = 'Yes'
    else: 
        smoke = 'No'
    #pet
    if RoomPF[3] > 0.5:
        pet = 'do'
    else:
        pet = 'don''t'
    #instrument
    if RoomPF[4] > 0.8:
        instrument = 'Guitar'
    elif RoomPF[4] > 0.6:
        instrument = 'Violin'
    elif RoomPF[4] > 0.4:
        instrument = 'Piano'
    elif RoomPF[4] > 0.2:
        instrument = 'Trumpet'
    else:
        instrument = 'None'
    #cleaning
    if RoomPF[5] > 0.8:
        clean = 'Daily'
    elif RoomPF[5] > 0.5:
        clean = 'Weekly'
    elif RoomPF[5] > 0.2:
        clean = 'Biweekly'
    else:
        clean = 'I don''t know how to clean'
    #cook
    if RoomPF[6] > 0.8:
        cook = 'I''m basically a commercial chef'
    elif RoomPF[6] > 0.5:
        cook = 'I''m better than average'
    elif RoomPF[6] > 0.2:
        cook = 'I''m average'
    else:
        cook = 'I don''t know how to cook'
    #friends
    if RoomPF[7] > 0.7:
        friends = 'I have freinds over alot'
    elif RoomPF[7] > 0.4:
        friends = 'I have friends over occasionaly'
    else:
        friends = 'I rarely have friends over'
    #wake
    if RoomPF[8] > 0.7:
        wake = 'I wake up before 8am'
    elif RoomPF[8] > 0.4:
        wake = 'I wake up before 10am'
    else:
        wake = 'I wake up eventually'
    #sleep
    if RoomPF[9] > 0.8:
        sleep = 'I go to bed eventually'
    elif RoomPF[9] > 0.5:
        sleep = 'I go to bed by midnight'
    elif RoomPF[9] > 0.3:
        sleep = 'I go to bed by 10pm'
    else:
        sleep = 'I''m in bed by 8pm'
    #decorate
    if RoomPF[10] > 0.5:
        decorate = 'I need to decorate everything'
    else:
        decorate = 'I don''t care much for decorations'
    #noise
    if RoomPF[11] > 0.7:
        noise = 'I tend to be quite noisy'
    elif RoomPF[11] > 0.4:
        noise = 'I don''t tend to make much noise'
    else:
        noise = 'I''m as quiet as a mouse'
    profile = interface.request_user_profile_from_backend()
    return render_template('index.html', name=profile.name, 
    age=profile.age, location=profile.location, 
    bio=profile.bio, pfimg=profile.profile_picture,
    smoke=smoke,
    pet=pet,
    instrument=instrument,
    clean=clean,
    cook=cook,
    friends=friends,
    wake=wake,
    sleep=sleep,
    decorate=decorate,
    noise=noise)
    
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
    backend.dataLoad(RoomPF, 1.0)
    RoomPF = backend.getProfile()
    return redirect('/swipe')

@app.route('/dislike', methods = ['POST'])
def dislike():
    global RoomPF
    backend.dataLoad(RoomPF, 0.0)
    RoomPF = backend.getProfile()
    return redirect('/swipe')

if __name__ == '__main__':
    app.run()


