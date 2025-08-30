from app import app
from flask import render_template

@app.route('/')
def hrllo():
    user= {'username': 'Hariom'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)