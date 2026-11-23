from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

REDIRECT_URLS = {
    "android": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-Android-2.2.apk",
    "pc": "https://github.com/mrdasher-col/expert-carnival/releases/download/Production/Custom.GD.layouts-PC-2.2.zip",
}


def _resolve_redirect(request: Request) -> RedirectResponse:
    candidates = [
        request.url.path,
        request.headers.get("x-matched-path", ""),
        request.headers.get("x-now-route-matches", ""),
        request.headers.get("x-invoke-path", ""),
    ]
    combined = " ".join(candidates).lower()

    if "/android" in combined or combined.endswith("android"):
        return RedirectResponse(url=REDIRECT_URLS["android"], status_code=302)
    if "/pc" in combined or combined.endswith("pc"):
        return RedirectResponse(url=REDIRECT_URLS["pc"], status_code=302)

    raise HTTPException(status_code=404, detail="Not Found")


@app.get("/android")
@app.get("/pc")
@app.get("/api/index")
@app.get("/{full_path:path}")
def redirect_handler(request: Request, full_path: str = ""):
    return _resolve_redirect(request)
