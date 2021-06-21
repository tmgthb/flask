from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Start Page'

@app.route('/info/')
def info():
    return 'Info'

if __name__ == '__main__':
    app.run()


