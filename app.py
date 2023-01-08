from flask import Flask, render_template, redirect, request
import interface
from save import *
from user_profile import *

app = Flask(__name__)

name = 'Karen'
age = '30'
bio = 'I like dogs'
location = 'Kentucky'
profile_image = './static/testprofile.png'
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
    profile = load_user_profile(name)
    print(profile)
    if profile == None:

        profile = user_profile()
        profile.name = name
        profile.age = 42
        profile.bio = "This is an interesting biography of a new user of this site"
        save_user_profile(name, profile)

    return redirect('/swipe')

if __name__ == '__main__':
    app.run()


