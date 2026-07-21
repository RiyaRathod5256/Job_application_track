from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException
from app.services.auth import validate_session,user_required
from app.schema.schema import Company
from app.services.save_job import save_job_db
company_router=APIRouter()

@company_router.post("/job/save")
async def save__company_job(user_id=Depends(validate_session),job:Company|None=Body()):
      
      role=user_required(user_id)

      result=save_job_db(job,user_id)

      if result:
            return{"message":"Saved job successfully"}
      raise HTTPException(status_code=400,detail="Unable to save job")
      

      


    


