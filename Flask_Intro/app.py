from flask import Flask, render_template, request 
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

# Replace these values with your email server information
EMAIL_ADDRESS = "ronalyndavid1013@gmail.com"
EMAIL_PASSWORD = "Prettygirl101303"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert', methods=['POST'])
def convert():
    user_input = request.form['user_input']
    uppercase_input = user_input.upper()
    return render_template('touppercase.html', uppercase_input=uppercase_input)

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

@app.route("/", methods=["GET", "POST"])
def triangle_area():
    if request.method == "POST":
        side_a = float(request.form["side_a"])
        side_b = float(request.form["side_b"])
        side_c = float(request.form["side_c"])
        triangle_area = calculate_triangle_area(side_a, side_b, side_c)
        return render_template("areatriangle.html", triangle_area=triangle_area)
    return render_template("areatriangle.html", triangle_area=None)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Works.html', result=result)
@app.route('/touppercase')
def touppercase():
    return render_template('touppercase.html')

@app.route('/areacircle')
def areacircle():
    return render_template('areacircle.html')

@app.route('/areatriangle')
def areatriangle():
    return render_template('areatriangle.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = EmailMessage()
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg['Subject'] = f"Contact Form Submission from {name}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
        except Exception as e:
            # Handle any email sending errors here
            print(e)
            return "Error sending email"

        return "Email sent successfully"

    return render_template('Contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
