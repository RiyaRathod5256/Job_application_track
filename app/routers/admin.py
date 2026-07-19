from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException,Cookie
from app.services.auth import validate_session
from app.database import get_connection
admin_router=APIRouter()

@admin_router.get("/admin/users/")
async def get_all_users(Session_id:str=Cookie(),user_id=Depends(validate_session)):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""select u.user_id,u.username,u.useremail,count(j.app_id) as total_applications
                   from users as u LEFT JOIN job_applications as j 
                   ON u.user_id = j.user_id
                   group by 
                   u.user_id""")
                   
    users=cursor.fetchall()
    return users


    