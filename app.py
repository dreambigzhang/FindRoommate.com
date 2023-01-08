from flask import Flask, render_template, redirect

app = Flask(__name__)

name = 'Karen'
age = '30'
bio = 'I like dogs'
location = 'Kentucky'
profile_image = './static/testprofile.png'
@app.route('/')
def main():
    return render_template('index.html', name=name, age=age, location=location, bio=bio, pfimg = profile_image)

@app.route('/run-dislike-script')
def run_dislike_script():
    print('Dislike')

@app.route('/liked')
def new():
    return render_template('liked.html')

if __name__ == '__main__':
    app.run()


