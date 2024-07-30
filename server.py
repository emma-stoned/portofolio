from flask import Flask, render_template, url_for, request, redirect
import csv
# web-server\Scripts\activate
# flask --app hello run
# flask --app hello run --debug
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('website.html')


@app.route("/<string:page_name>")
def redirecting_page(page_name):
    return render_template(page_name)


def write_to_csv(database):
    with open('database3.csv', mode='a') as database3:
        email = database['email']
        message = database['message']
        name = database['name']
        csv_writer = csv.writer(database3, delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,
                            name, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'something went wrong'
