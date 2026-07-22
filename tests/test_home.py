def test_home(client):

    response=client.get("/")
    
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:")
    print(response.text)

    assert response.status_code==200
    

