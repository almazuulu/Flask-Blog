from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Main Page!</h1>"

@app.route("/about")
def about_page():
    return "<h1>About page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
