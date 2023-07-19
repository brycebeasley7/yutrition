from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key = True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_create =  db.Column(db.DateTime, default=datetime.utcnow)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def user():
    users = User.query.order_by(User.date_create).all()
    return render_template('user.html', users=users)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/subscription')
def subscription():
    return render_template('subscription1.html')

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        fName = request.form['firstname']
        lName = request.form['lastname']
        userName = request.form['userName']
        passWord = request.form['passWord']
        new_user = User(
            fname=fName, 
            lname=lName, 
            username=userName, 
            password=passWord
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
        except:
            return "something didn't work. "
    else: 
        users = User.query.order_by(User.date_create).all()
        return render_template('index.html', users=users)



@app.route('/service.html')
def service():
    users = User.query.order_by(User.date_create).all()
    return render_template('service.html', users=users)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)