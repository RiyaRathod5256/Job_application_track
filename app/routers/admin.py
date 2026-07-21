from fastapi import APIRouter,Response,Depends,Request,Body,HTTPException,Cookie,Path
from app.services.auth import validate_session,admin_required
from app.database import get_connection
admin_router=APIRouter()
from datetime import datetime,UTC

@admin_router.get("/admin/users/")
async def get_all_users(Session_id:str=Cookie(),user_id=Depends(validate_session)):

    role=admin_required(user_id)

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""select u.user_id,u.username,u.useremail,count(j.app_id) as total_applications
                   from users as u LEFT JOIN job_applications as j 
                   ON u.user_id = j.user_id
                   group by 
                   u.user_id
                   order by 
                   u.user_id Asc""")
                   
    users=cursor.fetchall()
    

    result = []
    print(users)
    for user in users:
        result.append({
        "id": user[0],
        "username": user[1],
        "email": user[2],
        "total_applications": user[3]
    })

    print(result)
    return result
    

@admin_router.get("/admin/applications")
async def get_applications(Session_id:str=Cookie(),user_id=Depends(validate_session)):
   try:
    role=admin_required(user_id)
    conn=get_connection()
    cursor=conn.cursor()
    
    cursor.execute("""select users.username,companies.company_name,job_applications.job_status,job_applications.applied_date
          from users 
                   join job_applications
          on users.user_id=job_applications.user_id 
          join companies 
          on job_applications.company_id=companies.company_id
          ORDER BY job_applications.applied_date DESC""")
    
    data=cursor.fetchall()

    applications=[]
    
    for d in data:
        applications.append({
            "username":d[0],
            "company":d[1],
            "status":d[2],
            "date":d[3]

    })
        
    return applications
     
   except Exception as e:
      print(e)
      raise HTTPException(status_code=500,details="internal server error")
   
   finally:
      cursor.close()
      conn.close()

@admin_router.delete("/admin/users/{id}")
async def delete_user(id:str=Path(),user_id=Depends(validate_session)):
   role=admin_required(user_id)
   try:
      conn=get_connection()
      cursor=conn.cursor()

      cursor.execute("delete from sessions where user_id=%s",(id,))
      cursor.execute("delete from job_applications where user_id=%s",(id,))
      cursor.execute("delete from users where user_id=%s",(id,))
      conn.commit()
      return "deleted successfully"
   except Exception as e:
      print(e)
      raise
   finally:
      cursor.close()
      conn.close()
   
@admin_router.get("/admin/dashboard")
async def dashboard(user_id=Depends(validate_session)):
   role=admin_required(user_id)
   try:
      conn=get_connection()
      cursor=conn.cursor()

      cursor.execute("select count(app_id) from job_applications;")
      data=cursor.fetchone()
      total_applications=data[0]

      cursor.execute("select count(user_id) from users;")
      data=cursor.fetchone()
      total_users=data[0]

      date=datetime.now(UTC)
      
      cursor.execute("select count(app_id) from job_applications where applied_date=%s",(date,))
      data=cursor.fetchone()
      today_applications=data[0]

      cursor.execute("""select users.username,companies.company_name,job_applications.job_status,job_applications.applied_date
          from users 
                   join job_applications
          on users.user_id=job_applications.user_id 
          join companies 
          on job_applications.company_id=companies.company_id
          ORDER BY job_applications.applied_date DESC
                     LIMIT 5""")
    
      data=cursor.fetchall()

      recent_applications=[]
    
      for d in data:
        recent_applications.append({
            "username":d[0],
            "company":d[1],
            "status":d[2],
            "date":d[3]

    })

      return({
         "total_users":total_users,
         "total_applications":total_applications,
         "today_applications":today_applications,
         "recent_applications":recent_applications,
          
      })
      





   except Exception as e:
      print(e)
      raise

   
   

