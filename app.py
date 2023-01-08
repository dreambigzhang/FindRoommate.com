from flask import Flask, render_template, redirect, request
import interface
from save import *
from user_profile import *
from gradientDescent import MLBackend
app = Flask(__name__)
backend = MLBackend()
UserPF = []

@app.route('/')
def main():
    return render_template('landing.html')

@app.route('/swipe')
def start():
    profile = interface.request_user_profile_from_backend()
    return render_template('index.html', name=profile.name, age=profile.age, location="None", bio=profile.bio, pfimg=profile.profile_picture)

@app.route('/refresh')
def refresh():
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verify', methods=['POST'])
def verify():
    name = request.form['name']
    print(name)
    UserPF = backend.getProfile()
    return redirect('/swipe')
    # profile = load_user_profile(name)
    # print(profile)
    # if profile == None:
    #     pass

@app.route('/like', methods = ['POST'])
def like():
    print('like')
    backend.dataLoad(UserPF, 1)
    return redirect('/swipe')

@app.route('/dislike', methods = ['POST'])
def dislike():
    print('dislike')
    backend.dataLoad(UserPF, 0)
    return redirect('/swipe')

if __name__ == '__main__':
    app.run()


