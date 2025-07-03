from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from mirror.utils_core import update_message, get_message  # updated import path

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/control")
def load_control_page(request: Request):
    message = get_message("A")
    return templates.TemplateResponse("pageA.html", {"request": request, "message": message})

@router.post("/sync")
def sync_message(message: str = Form(...)):
    update_message("A", message)
    return RedirectResponse("/control", status_code=302)


