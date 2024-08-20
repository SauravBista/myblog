from flask import Flask, render_template, request
import requests
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/9a5c56ca865bf0772ebb").json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        username = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        #Sending the mail
        msg = MIMEMultipart()
        msg_body = f"name: {username} \n email: {email} \n phone: {phone} \n message: {message}"
        msg.attach(MIMEText(msg_body, 'plain'))
        my_email = os.environ.get('my_email')
        password = os.environ.get('my_password')
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection .sendmail(from_addr=my_email, to_addrs=email, msg=msg.as_string())
        return render_template("contact.html", message=True)
    else:
        return render_template("contact.html", message=False)


if __name__ == "__main__":
    app.run(debug=True)