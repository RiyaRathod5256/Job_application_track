from fastapi import FastAPI,Request,Depends,Query,Body,Path
from app.database import get_connection
from app.routers.job_load import job_router
from app.routers.users import user_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.auth import validate_session,check_role,admin_required
from app.routers.company import company_router
from app.routers.admin import admin_router
from app.services.save_job import my_applications
from app.routers.application import application_router
from app.services.Applications import update_app_status
from app.services.Applications import delete_app_status
from app.schema.schema import UpdateStatus



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(job_router)
app.include_router(user_router)
app.include_router(company_router)
app.include_router(application_router)
app.include_router(admin_router)

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

@app.get("/dashboard")
def dashboard(request: Request,user=Depends(validate_session)):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )

@app.patch("/applications/{id}")
def update_status(status:UpdateStatus,id:str|None=Path(),user_id=Depends(validate_session),):
    result=update_app_status(id,status.job_status,user_id)

@app.delete("/applications/{id}")
def update_status(id:str|None=Path(),user_id=Depends(validate_session)):
    result=delete_app_status(id,user_id)

@app.get("/admin")
def get_admin(request:Request,user_id=Depends(validate_session)):
    role=admin_required(user_id)
    return templates.TemplateResponse(
        "admin.html",
        {"request": request}
    )






