
#give correct username 
def test_register_username_length_pass(client):

    payload = {
        "username": "Riya_1234",
        "useremail": "R@gmail.com",
        "userphonenumber": "9876543910",
        "userpassword": "Pass@123",
        "confirmpassword":"Pass@123"
    }

    response=client.post("/register/",json=payload)
    
    assert response.status_code==409
    
    

    
    
#test_to_fail- username length
def test_register_username_length_fail(client):

    payload = {
            "username": "Ri",
            "useremail": "jiya@gmail.com",
            "userphonenumber": "9865543210",
            "userpassword": "Pass@123",
            "confirmpassword":"Pass@123"
        }
    response=client.post("/register/",json=payload)
    
    assert response.status_code==422

#use special character in username
def test_register_username_specialchar_fail(client):

    payload={
            "username": "Ri@456677",
            "useremail": "kiya@gmail.com",
            "userphonenumber": "9876543210",
            "userpassword": "Pass@123",
            "confirmpassword":"Pass@123"
        }

    response=client.post("/register/",json=payload)
        
    assert response.status_code==422

#username start with digit
def test_register_username_startwithdigit_fail(client):

    payload={
            "username": "345riya",
            "useremail": "piya@gmail.com",
            "userphonenumber": "9876543210",
            "userpassword": "Pass@123",
            "confirmpassword":"Pass@123"
        }

    response=client.post("/register/",json=payload)
        
    assert response.status_code==422




def test_register_username_maxlength_fail(client):

    payload={
            "username": "bfbmgbngbgkbjhiojiohtyihjhnngbgbnbmgfnbmmbiturntjrbbbbbbbbbbbbbbbbbbbbiiiiiiiiiiiiiiiiiiiiiiiiiiiiinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggtiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
            "useremail": "hiya@gmail.com",
            "userphonenumber": "9878543210",
            "userpassword": "Pass@123",
            "confirmpassword":"Pass@123"
        }

    response=client.post("/register/",json=payload)
        
    assert response.status_code==422 

def test_register_username_usespace_fail(client):

    payload={
            "username": "Riya Rathod ",
            "useremail": "ifya@gmail.com",
            "userphonenumber": "9876543210",
            "userpassword": "Pass@123",
            "confirmpassword":"Pass@123"
        }

    response=client.post("/register/",json=payload)
        
    assert response.status_code==422 


def test_register_username_repeatativechar_fail(client):

    payload={
                "username": "rrrrrr",
                "useremail": "griyu@gmail.com",
                "userphonenumber": "9876810978",
                "userpassword": "Pass@123",
                "confirmpassword":"Pass@123"
            }
    response=client.post("/register/",json=payload)
            
    assert response.status_code==422 



def test_register_username_doubleunderscore_fail(client):

    payload={
                    "username": "ram__",
                    "useremail": "ram@gmail.com",
                    "userphonenumber": "9876348810",
                    "userpassword": "Pass@123",
                    "confirmpassword":"Pass@123"
                }
    response=client.post("/register/",json=payload)
                
    assert response.status_code==422 







   


