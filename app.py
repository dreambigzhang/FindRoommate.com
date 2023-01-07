from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/run-like-script')
def run_like_script():
    print('Like')
    #result = 'Like!'
@app.route('/run-dislike-script')
def run_dislike_script():
    print('Dislike')


if __name__ == '__main__':
    app.run()


