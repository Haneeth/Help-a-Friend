from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '7189637288d07bd7874d04d33d95060e'

posts =[
	{
	'author':'haneeth',
	'title' : 'cricbuzz',
	'content' : 'cricket updates',
	'date_posted' : 'lastest july'
	},
	{
	'author':'lanja',
	'title' : 'cricbuzz 1',
	'content' : 'cricket updates 1',
	'date_posted' : 'lastest july 1'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=posts)


@app.route("/about")
def about():
	return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Profile created for {form.username.data}!','success')
		return redirect(url_for('home'))

	return render_template('register.html',title='Register',form=form)


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@google.com' and form.password.data == 'password':
			flash('Logged in!' , 'success')
			return redirect(url_for('home'))
		else:
			flash('login creds invalid','danger')
	return render_template('login.html',title='Login',form=form)



if __name__ == '__main__':
	app.run(debug=True)