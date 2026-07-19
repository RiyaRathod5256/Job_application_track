from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException
from app.services.auth import validate_session,user_required
from app.services.Applications import my_applications
 
application_router=APIRouter()


@application_router.get("/applications")
def get_applications(user_id=Depends(validate_session)):
    role=user_required(user_id)
    applications=my_applications(user_id)
    return applications

