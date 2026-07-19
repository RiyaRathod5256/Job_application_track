from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException
from app.services.auth import validate_session
from app.services.Applications import my_applications
 
application_router=APIRouter()


@application_router.get("/applications")
def get_applications(user_id=Depends(validate_session)):
    applications=my_applications(user_id)
    return applications

