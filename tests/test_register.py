
#give correct username 
def test_register_pass(client):
    payload = {
        "username": "john_1234",
        "useremail": "john@gmail.com",
        "userphonenumber": "9876543210",
        "userpassword": "Pass@123"
    }

    response=client.post("/register/",json=payload)
    
    assert response.status_code==200
    assert response.json()=={
        "msg": " user registered successfully"
    }

    
    
#test_to_fail
def test_register_fail(client):
    payload = {
            "username": "jo",
            "useremail": "john@gmail.com",
            "userphonenumber": "9876543210",
            "userpassword": "Pass@123"
        }
    response=client.post("/register/",json=payload)
    
    assert response.status_code==200
    assert response.json()=={
        "msg": " user registered successfully"
    }


