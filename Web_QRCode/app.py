from flask import Flask, render_template, redirect, request as rq
import qrcode
from random import randint
from time import time
import os

# functions
def createQRCode(content, fg, bg):
    global data

    file = f"static/qrcode/qrcode-{randint(1, 100000000)}-inTime{time()}.png"
    qr = qrcode.QRCode(version=1)
    qr.add_data(content)
    qr.make(fit = True)
    img = qr.make_image(fill_color=fg , back_color=bg)
    img.save(file)
    data["file"] = file
    print(data)

def delete():
    os.remove(data["file"])


app = Flask(__name__)

data = {
    "file" : ""
}

# route
@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    data = rq.form.get("data")
    qrcode_bg = rq.form.get("bg")
    qrcode_fg = rq.form.get("fg")
    createQRCode(data, qrcode_fg, qrcode_bg)
    return redirect("/")

@app.route("/delete", methods=["GET", "POST"])
def delete_qrcode():
    delete()
    return redirect("/")

# run
if __name__ == "__main__":
    app.run(debug=True)
