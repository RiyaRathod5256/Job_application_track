import secrets
from app.database import get_connection
from datetime import datetime, timedelta, UTC
from fastapi import Cookie,HTTPException,Request

def create_session(user_id):
    

    
    try:
    #insert userid and session id into database
        conn=get_connection()
        cursor=conn.cursor()

        login_time=datetime.now(UTC)
        expires_at=login_time + timedelta(days=15)
        print("login_time and expires_time",login_time,expires_at)
        
        session_id=generate_session_id()
        print(session_id)
        cursor.execute("insert into sessions (session_id,user_id,expires_at) values (%s,%s,%s)",(session_id,user_id,expires_at))
        conn.commit()

        print("User:",user_id)
        print("session:",session_id)

        return session_id
    except Exception as e:
        print("error",e)

    finally:
        
        cursor.close()
        conn.close()
        

        

def generate_session_id():
    return secrets.token_hex(32)

def validate_session(Session_id:str|None=Cookie(default=None)):
      
      conn=get_connection()
      cursor=conn.cursor()
      
      

      if not Session_id:
           raise HTTPException(status_code=401,detail="login required")
      
      cursor.execute("select user_id,session_id,expires_at from sessions where session_id=%s",(Session_id,))
      session=cursor.fetchone()


      user_id = session[0]
      expires_at = session[1]
      print(type(expires_at))
      

      if not session:
              raise HTTPException(
            status_code=401,
            detail="Invalid session"
        )


      if datetime.now() > expires_at:
        print("Session expired")
        return {"msg":"session_expired"}
      

      if not session:
              raise HTTPException(
            status_code=401,
            detail="Invalid session"
        )
      else:
        return user_id
           
      
def session_pop(Session_id):
      print("Cookie:", Session_id)
      conn=get_connection()
      cursor=conn.cursor()
      
      cursor.execute("select session_id from sessions where session_id=%s",(Session_id,))
      session_id=cursor.fetchone()
      print(session_id)

      if not session_id:
           raise HTTPException(status_code=401,detail="Invalid session.")

           
      cursor.execute("delete from sessions where session_id=%s",(Session_id,))
      conn.commit()
      cursor.close()
      return {"msg":"log out"}



