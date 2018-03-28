from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello world"

@app.route('/hello')
def hell_world():
    return 'hellow world'

if __name__ == "__main__":
#    app.debug = True
    app.run()
#    app.run(debug = True)
