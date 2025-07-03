from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse, RedirectResponse
from mirror.utils_core import get_message
from pages import page_a, page_b

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include route handlers
app.include_router(page_a.router)
app.include_router(page_b.router)

@app.get("/")
async def redirect_based_on_domain(request: Request):
    host = request.headers.get("host", "")
    if "pulsea.live" in host:
        return RedirectResponse(url="/control")  # Corrected: Page A
    elif "pulseb.live" in host:
        return RedirectResponse(url="/stream")   # Correct: Page B
    return PlainTextResponse("Unknown domain", status_code=400)

@app.get("/api/message/from/{origin}", response_class=PlainTextResponse)
def api_get_message(origin: str):
    if origin in ("A", "B"):
        return get_message(origin)
    return "Invalid origin."
