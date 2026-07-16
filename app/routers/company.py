from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException
from app.services.auth import validate_session
from app.schema.schema import Company
from app.services.company_data import save_job_db
company_router=APIRouter()

@company_router.post("/job/save")
async def save__company_job(user=Depends(validate_session),job:Company|None=Body()):
      result=save_job_db(job,user["user_id"])

      if result:
            return("Saved job successfully")
      raise HTTPException(status_code=400,detail="Unable to save job")
      


    


