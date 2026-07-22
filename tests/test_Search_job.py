def test_Search(client):
    response=client.get("/Search_job")
    assert response.status_code==200