from fastapi import FastAPI,Request,Depends
from app.database import get_connection
from app.routers.job_load import job_router
from app.routers.users import user_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.auth import validate_session

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(job_router)
app.include_router(user_router)

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@app.get("/Search_job")
async def home(request: Request):
    return templates.TemplateResponse(
        "Search_job.html",
        {"request": request}
    )

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )

@app.get("/dashboard")
async def dashboard(
    request: Request,
    user=Depends(validate_session)
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user
        }
    )

@app.get("/jobs")
async def jobs_page(
    request: Request,
    user=Depends(validate_session)
):
    return templates.TemplateResponse(
        "Search_job.html",
        {
            "request": request,
            "user": user
        }
    )


