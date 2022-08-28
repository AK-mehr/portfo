# Activating venv in cmd: Scripts\activate.bat
# directory -> C:\Users\alire\PycharmProjects\pythonGithubProjects\web server\venv>

# Run Flask: flask --app <server name> --debug run
# directory -> C:\Users\alire\PycharmProjects\pythonGithubProjects\web server>

from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)


def write_to_database(data):
    email = data['email']
    text = data['text']
    message = data['message']
    with open('./database', mode='a') as db:
        db.write(f'\n{email}, {text}, {message}')


def write_to_csv(data):
    email = data['email']
    text = data['text']
    message = data['message']
    with open('./database.csv', newline='', mode='a') as db2:
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, text, message])


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/<string:pages_name>")
def page_name(pages_name):
    return render_template(pages_name)


@app.route("/submit_form", methods=['POST', 'GET'])
def submitted_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save into database!'
    else:
        return f'Something went wrong, try again'



