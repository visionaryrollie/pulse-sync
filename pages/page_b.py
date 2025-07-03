from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from mirror.utils_core import get_message, update_message  # updated import path

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/stream")
def load_stream_page(request: Request):
    message = get_message("B")
    return templates.TemplateResponse("pageB.html", {"request": request, "message": message})

@router.post("/send_stream")
def send_message_from_b(message: str = Form(...)):
    update_message("B", message)
    return RedirectResponse("/stream", status_code=302)



