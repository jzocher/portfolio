from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db2:
        email = data['email']
        name = data['name']
        subject = data['msg_subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,subject,message])
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "Thank you! I will be in contact with you shortly"
        except:
            return 'Did not save to database'
    else:
        return 'There was an error'