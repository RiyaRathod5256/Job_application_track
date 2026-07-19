from app.database import get_connection
from datetime import datetime, timedelta, UTC
from fastapi import Cookie,HTTPException,Request




def my_applications(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""select j.app_id,
                    c.company_name,c.company_location,j.job_role,j.job_status,
                   j.applied_date,c.website,c.salary from job_applications as j join companies as c 
                    on
                    j.company_id=c.company_id where j.user_id =%s
                    order by j.applied_date Desc 
                   
        
    """,(user_id,))

    jobs = cursor.fetchall()

    applications=[]
    for job in jobs:
        applications.append({
           "app_id":job[0],
            "company_name":job[1],
            "company_location":job[2],
            "job_role":job[3],
            "job_status":job[4],
            "job_applied_date":str(job[5]),
            "website":job[6],
            "salary":job[7]
        })

    
    
    cursor.close()
    conn.close()
    return applications

def update_app_status(id,status,user_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE job_applications set job_status=%s where app_id=%s and user_id=%s",(status,id,user_id))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return e
    

def delete_app_status(id,user_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("Delete from job_applications where app_id=%s and user_id=%s",(id,user_id))
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return e
    

