from fastapi import APIRouter,Depends
from app.services.jooble_service import search_jobs
from app.services.auth import validate_session,user_required

job_router=APIRouter(prefix="/jobs",tags=["Jobs"])

@job_router.get("/job_load")
async def get_jobs(keyword:str,location:str,user_id=Depends(validate_session)):
    role=user_required(user_id)

    Jobs_data=await search_jobs(keyword,location)
    
    return Jobs_data


