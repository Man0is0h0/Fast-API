from app import schemas,utils
from .database import client,session
def test_root(client):
    res=client.get("/")
    print(res.json().get('Message: '))
    # print(res.json())
    assert (res.json().get('Message: '))== "Welcome to my api!!!"
    assert res.status_code==200

def test_create_user(client,session):
    res=client.post("/users",json={"email":"hello123@gmail.com","password":"password123"})
    user=schemas.UserSend(**res.json())
    print(res.json())
    print("History:", res.history)
    print("Final status:", res.status_code)
    assert user.email=="hello123@gmail.com"
    assert res.status_code==201

def test_login_user(client):
    res=client.post('/login',data={"username":"hello123@gmail.com","password":"password123"})
    print(res.json())
    assert res.status_code==200