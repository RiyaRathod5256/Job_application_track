from app.database import get_connection
from pwdlib import PasswordHash
from fastapi import HTTPException
from app.services.auth import create_session

password_hash=PasswordHash.recommended()
#USER REGISTRATION
def register_user(user):
    
    conn=get_connection()
    print(conn)
    cursor=conn.cursor()
    try:
         #useremail exist
         cursor.execute("select useremail from users;")
         users=cursor.fetchall()
         print(users)
         print(user)
         if user.useremail in users:
              raise HTTPException(status_code=409,detail={
        "field":"useremail",
        "message":"Email already exists."
    }
)
           
         
         #username exist
         cursor.execute("SELECT 1 FROM users WHERE username=%s",(user.username,))

         if cursor.fetchone():
             raise HTTPException( status_code=409,detail={
            "field":"username",
            "message":"Username already exists."
        })
        
         else:
             password=password_hash.hash(user.userpassword)
             cursor.execute("insert into users(username,useremail,userphonnumber,userpassword) Values(%s,%s,%s,%s)",(user.username,user.useremail,user.userphonenumber,password))
         conn.commit()
         print("data inserted")
         cursor.close()
         conn.close

    except HTTPException:
         raise
    except Exception :

        conn.rollback()
        raise HTTPException(
        status_code=500,
        detail="Internal Server Error"
    )
    return {"msg":" user registered successfully"}

#USER LOGIN
async def login_user(credential):
  try:

        conn=get_connection()
        cursor=conn.cursor()

        username=credential.username
        password=credential.userpassword

        
        cursor.execute(f"select username from users where username=%s",(username,))
        user=cursor.fetchone()
        print(user)

        if user:
            cursor.execute(f"select userpassword from users where username=%s",(username,))
            hash_password=cursor.fetchone()
            if(password_hash.verify(password,hash_password[0])):
                cursor.execute("select user_id from users where username=%s",(username,)) 
                user_id=cursor.fetchone() 
                print("user_id is :",user_id[0])
                session_id=create_session(user_id[0])
                return session_id
            else:
                raise HTTPException(status_code=402,detail={
                    "field":"userpassword",
                    "message":"Incorrect password."
                })
        else:
                raise HTTPException(status_code=404,detail={
                    "field":"username",
                    "message":"User not found."})
                
  except HTTPException:
        raise
        
  except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )  

  finally:   
         conn.close()
         cursor.close()

    #Session Creation





