from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
from mirror.utils_core import get_message
from pages import page_a, page_b

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include route handlers
app.include_router(page_a.router)
app.include_router(page_b.router)

@app.get("/api/message/from/{origin}", response_class=PlainTextResponse)
def api_get_message(origin: str):
    if origin in ("A", "B"):
        return get_message(origin)
    return "Invalid origin."