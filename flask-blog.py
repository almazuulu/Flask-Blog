from crypt import methods
from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']= '7b85c50c92d0235dbd20a4d07d008e7c'

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
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title = 'About page')

@app.route("/register", methods=['GET', 'POST'])
def register_form():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')  
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login_form():
    form  = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data=="password":
            flash('You have been loged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccussful. Please check username or password!', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)
