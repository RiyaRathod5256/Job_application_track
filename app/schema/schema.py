from pydantic import BaseModel,Field,field_validator,EmailStr,model_validator,HttpUrl
import re

class User(BaseModel):
    username:str=Field(min_length=3,max_length=70,pattern=r"^[A-Za-z_][A-Za-z0-9_]*$",description="username must start with _ or letter and does not contain special character")
    userpassword:str=Field(min_length=8,max_length=8,description="password must be of 8 character ,must contain one capital one small one special and one digit")
    confirmpassword:str=Field(min_length=8,max_length=8,description="password must be of 8 character ,must contain one capital one small one special and one digit")

    useremail:EmailStr
    userphonenumber:str=Field(min_length=10,max_length=10,pattern=r"^[6-9]\d{9}$")

    @field_validator("username")#it says that you must validate this field before creation
    @classmethod# give reference of class and make function classmethod
    def username_validate(cls,value):
        # pattern = r"^(?!.*(.)\1{5,})[A-Za-z_](?:[A-Za-z0-9]|_(?=[A-Za-z0-9]))*$"
        pattern=r"^(?!.*__)(?!.*(.)\1{5,})[A-Za-z_](?:[A-Za-z0-9]|_(?=[A-Za-z0-9]))*$"

        if not re.fullmatch(pattern, value): # match the pattern with given value
            raise ValueError("Invalid username")
        
        return value
    
    @field_validator("useremail")
    @classmethod
    def validate_email_length(cls, value):
        if len(str(value)) > 254:
            raise ValueError("Email cannot exceed 254 characters")
        return value
    
    @field_validator("userpassword")
    @classmethod
    def password_validate(cls,value):
        if not re.search(r"[A-Z]",value):
            raise ValueError("Password must contain one Capital letter")
        if not re.search(r"[a-z]",value):
            raise ValueError("Password must contain one small letter")
        if not re.search(r"[0-9]",value):
            raise ValueError("Password must contain one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            raise ValueError("Password must conatin special character")
        return value
    
    @field_validator("userphonenumber")
    @classmethod
    def phonenumber_validate(cls,value):
        for digit in value:
           if value.count(digit)>5:
               raise ValueError("No digit can ne repeated more than 5 times in phonenumber")
           return value
        
    @model_validator(mode="after")
    def password_match(self):
        if self.userpassword!=self.confirmpassword:
            raise ValueError("Password do not match")
        
        return self

 
class Userlogin(BaseModel):
    username:str=Field(min_length=3,max_length=70)
    userpassword:str=Field(min_length=8,max_length=8)
    
class Company(BaseModel):
    Jobrole:str
    company:str
    location:str
    jobtype:str|None
    salary:int|str|None
    website: HttpUrl
    
from pydantic import BaseModel

class UpdateStatus(BaseModel):
    job_status: str