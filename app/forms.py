from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


form_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@form_router.get("/offer-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("offer.html", {"request": request})


@form_router.get("/experience-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("experience.html", {"request": request})


@form_router.get("/hike-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("hike.html", {"request": request})


@form_router.get("/relieving-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("relieving.html", {"request": request})


@form_router.get("/resignation-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("resignation.html", {"request": request})


@form_router.get("/payslip-letter", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("payslip.html", {"request": request})
