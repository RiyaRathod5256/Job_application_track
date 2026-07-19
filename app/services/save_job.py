from app.database import get_connection
from datetime import datetime, timedelta, UTC
from fastapi import Cookie,HTTPException,Request


def save_job_db(job,user_id):
    if not job:
        print("job object i not present")
    if not user_id:
        print("user is not present")

    company_name=job.company
    company_location=job.location
    job_role=job.jobtype
    salary=job.salary
    website=str(job.website)
    

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("select company_id from companies where company_name=%s",(company_name,))
    company=cursor.fetchone()
    print(company)
    if company:
        print("msg:""company already exist")
        
    else:
        cursor.execute("insert into companies(company_name,company_location,website,salary) values (%s,%s,%s,%s)",(company_name,company_location,website,salary))
        cursor.execute("select company_id from companies where company_name=%s",(company_name,))
        company=cursor.fetchone()

    
    cursor.execute("insert into job_applications(user_id,company_id,job_role,job_status,job_location,applied_date) values (%s,%s,%s,%s,%s,%s)",(user_id,company[0],job_role,"applied",company_location,datetime.now(UTC)))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg":"saved_job"}

def my_applications(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""select job_application.app_id,
                    company_name,company_location,jobrole,jobstatus,
                   applied_date,website,salary from job_applications join companies on
                    job_application.company_id=companies.company_id where user_id ="%s"{user_id}
                    order by job_application.applied_date Desc
                   
        
    """,(user_id,))

    jobs = cursor.fetchall()

    applications=[]
    for job in jobs:
        applications.append({
           "app_id":job[0],
            "company_name":job[1],
            "website":job[2],
            "salary":job[3],
            "job_role":job[4],
            "job_status":job[5],
            "job_location":job[6],
            "applied_date":str(job[7])
        })

    
    conn.close()
    cursor.close()
    return applications

   