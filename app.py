from flask import Flask, request, render_template
import os
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Start Page'

@app.route('/info/')
def info():
    return render_template('info.html')
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port) #https://github.com/dpgaspar/Flask-AppBuilder/issues/733#issuecomment-379009480
    #app.run()


