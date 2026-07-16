from fastapi import APIRouter
from app.services.jooble_service import search_jobs

job_router=APIRouter(prefix="/jobs",tags=["Jobs"])

@job_router.get("/job_load")
async def get_jobs(keyword:str,location:str):
    Jobs_data=await search_jobs(keyword,location)

    return Jobs_data


