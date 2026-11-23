from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

URLS = {
    "android": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-Android-2.2.apk",
    "pc": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-PC-2.2.zip",
}


@app.get("/android")
def android_download():
    return RedirectResponse(url=URLS["android"], status_code=302)


@app.get("/pc")
def pc_download():
    return RedirectResponse(url=URLS["pc"], status_code=302)
