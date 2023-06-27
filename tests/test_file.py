from fastapi.testclient import TestClient
from api.main import app

client=TestClient(app)

def test_1():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()== {'message':'Hello World'}

# def test_2():
#     response = client.get("/list")

#     assert response.status_code == 200
#     assert len(response.json()['data'])==5

# def test_3():
#     response = client.get("/list/1")

#     assert response.status_code == 200
#     assert response.json()['data']== {'id':1,"name":'name1'}