from flask import Flask
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return 'Start Page'

@app.route('/info/')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run()


