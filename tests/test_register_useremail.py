def test_register_email_length_pass(client):

    payload={
                    "username": "Yuvi",
                    "useremail": "yuvi@gmail.com",
                    "userphonenumber": "8758345510",
                    "userpassword": "Pass@123",
                    "confirmpassword":"Pass@123"
                }
    

    response=client.post("/register/",json=payload)

    assert response.status_code==200

def test_register_email_yahoo_pass(client):

    payload={
                    "username": "Hriya",
                    "useremail": "hriya@yahoo.com",
                    "userphonenumber": "8701115765",
                    "userpassword": "Kagg@123",
                    "confirmpassword":"Kagg@123"
                }
    

    response=client.post("/register/",json=payload)

    assert response.status_code==200

def test_register_email_length_fail(client):

    payload={
        
                    "username": "Harshita",
                    "useremail":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.ccccccccccccccccccccccccccccccccccccccccccccccccccccccccc.com",
                    "userpassword": "Viri@123",
                    "confirmpassword":"Viri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_startdigit_fail(client):

    payload={
        
                    "username": "Harshitajihu",
                    "useremail": "444riya@gmail.com",
                    "userphonenumber": "7176226622",
                    "userpassword": "Kiri@123",
                    "confirmpassword":"Kiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==200

def test_register_email_empty_fail(client):

    payload={
        
                    "username": "",
                    "useremail": "4riya@gmail.com",
                    "userphonenumber": "7876348810",
                    "userpassword": "Biri@123",
                    "confirmpassword":"Biri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_spaces_fail(client):

    payload={
        
                    "username": "Yuvika",
                    "useremail": "  ",
                    "userphonenumber": "7876348810",
                    "userpassword": "Biro@123",
                    "confirmpassword":"Biro@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_missing_atrate_fail(client):
    payload={
        
                    "username": "Priyanka",
                    "useremail": "riyagmail.com",
                    "userphonenumber": "7876348810",
                    "userpassword": "Jirl@123",
                    "confirmpassword":"Jirl@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_missinglocaldomain_fail(client):

    payload={
        
                    "username": "youra",
                    "useremail": "@gmail.com",
                    "userphonenumber": "7870348810",
                    "userpassword": "Kiri@123",
                    "confirmpassword":"Kiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_missingdomain_fail(client):

    payload={
        
                    "username": "Jiyaka",
                    "useremail": "4riya@",
                    "userphonenumber": "7889348810",
                    "userpassword": "Piri@123",
                    "confirmpassword":"Piri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422


def test_register_email_missingtoplevel_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": "4riya@gmail",
                    "userphonenumber": "7876348810",
                    "userpassword": "Viri@123",
                    "confirmpassword":"Viri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_spaceinemail_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": "iya @gmail",
                    "userphonenumber": "7876348810",
                    "userpassword": "Kiri@123",
                    "confirmpassword":"Kiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_onlydigits_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": "977876435",
                    "userphonenumber": "7876348810",
                    "userpassword": "viri@123",
                    "confirmpassword":"viri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_traillingspace_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": "piya@gmail ",
                    "userphonenumber": "7876348810",
                    "userpassword": "Oiri@123",
                    "confirmpassword":"Oiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422


def test_register_email_startwithdot_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": ".riya@gmail",
                    "userphonenumber": "7876908810",
                    "userpassword": "Iiri@123",
                    "confirmpassword":"Iiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_missingtoplevel_fail(client):

    payload={
        
                    "username": "Siya",
                    "useremail": "4riya@gmail",
                    "userphonenumber": "7876348810",
                    "userpassword": "Piri@123",
                    "confirmpassword":"Piri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_Consecutivedots__fail(client):

    payload={
        
                    "username": "kiya",
                    "useremail": "riya..@gmail",
                    "userphonenumber": "7876348810",
                    "userpassword": "Oiri@123",
                    "confirmpassword":"Oiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_domainenddots__fail(client):

    payload={
        
                    "username": "kiya",
                    "useremail": "google@gmail.com.",
                    "userphonenumber": "7876348810",
                    "userpassword": "Liri@123",
                    "confirmpassword":"Liri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_Domainstartswithhyphen__fail(client):

    payload={
        
                    "username": "kiya",
                    "useremail": "riyo@_gmail.com",
                    "userphonenumber": "7876348810",
                    "userpassword": "Uiri@123",
                    "confirmpassword":"Uiri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

def test_register_email_Comma_instead_of_dot__fail(client):

    payload={
        
                    "username": "kiya",
                    "useremail": "riyo@gmail,com",
                    "userphonenumber": "8876348810",
                    "userpassword": "vOri@123",
                    "confirmpassword":"vOri@123"
                
    }

    response=client.post("/register/",json=payload)

    assert response.status_code==422

