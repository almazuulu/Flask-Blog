from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Askarbek Almazbek uulu',
        'title': 'My first blog',
        'content': 'First blog was created',
        'date_posted': 'June 12, 2022'
    },

    {
        'author': 'Adilet Eshmamatov',
        'title': 'My second blog',
        'content': 'Second blog is awesome',
        'date_posted': 'June 13, 2022'
    },

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title = 'About page')

if __name__ == '__main__':
    app.run(debug=True)
