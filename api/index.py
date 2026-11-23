from flask import Flask, redirect

app = Flask(__name__)

REDIRECT_URLS = {
    "/android": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-Android-2.2.apk",
    "/pc": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-PC-2.2.zip",
}


@app.route("/android")
def download_android():
    return redirect(REDIRECT_URLS["/android"], code=302)


@app.route("/pc")
def download_pc():
    return redirect(REDIRECT_URLS["/pc"], code=302)