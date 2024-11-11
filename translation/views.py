from pathlib import Path

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates_path = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=templates_path)


@router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
