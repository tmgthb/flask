from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    render_template('info.html')
@app.route("/info")
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run()
    
    
