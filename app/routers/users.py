from fastapi import APIRouter,Response,Depends,Request,Cookie
from app.schema.schema import User,Userlogin
from app.services.user_logic import register_user,login_user
from app.services.auth import validate_session,session_pop,check_role

user_router=APIRouter()

@user_router.post("/register/")
async def register(user:User):
    print(user)
    return register_user(user)
    
@user_router.post("/login/")
async def login(credential:Userlogin,response:Response):
    print(credential)

    session_id=await login_user(credential)

    print("sessionid:",session_id)
     #response is object which have 4 funtioncs of set_cookie,delete_cookie,headers,status code give response to browser
    response.set_cookie(key="Session_id",value=session_id,httponly=True,
        samesite="lax",
        secure=False,   # True when using HTTPS in production
        max_age=86400)
    print(response)
    print(response.headers)

    
    return{
        "msg":"Login Successfully"
    }



@user_router.get("/logout")
async def logout_user(response:Response,Session_id:str|None=Cookie()):
    print(Session_id)
    result=session_pop(Session_id)
    
    response.delete_cookie("Session_id")

    return {
        "msg": "Logged out successfully."
    }

