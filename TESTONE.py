# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp to say hello
"""
from flask import Flask, redirect, render_template, url_for # From 'flask' module import 'Flask' class/importing all the modules and import render template module
app = Flask(__name__)    # Construct an instance of Flask class for our webapp/object of ou webap

@app.route('/')   # decorator for routing methosesURL '/' to be handled by main() route handler (or view function) handle mapped ro the view function
def main():
    return render_template ('testone.html') #call the render template function from the falsk module

@app.route('/hello/<username>')  # URL with a variable
def hello_username(username):    # The function shall take the URL variable as parameter
    
    if username == "Lukman":
        return 'Hello, {}'.format(username)
    else:
        return redirect(url_for('main'))

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp
    