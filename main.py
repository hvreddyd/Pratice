#importing the lib
from flask import Flask ,render_template

#initalizing the app
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/images')
def images():
    return "This is the image page"

@app.route('/contact')
def contact():
    return "This is the contact page"

@app.route('/aboutus')
def aboutus():
    return "This is the About us  page"

app.run()
#should always have it to run and always at the end of the code.

