from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('day2.html')

@app.route('/data', methods=['post'])
def data():
    firstname = request.form.get('first_name')
    secondname = request.form.get('second_name')
    phonenr = request.form.get('phone number')
    email = request.form.get('email')
    print(firstname,secondname,phonenr,email)
    return 'data received'
app.run(debug=True)

