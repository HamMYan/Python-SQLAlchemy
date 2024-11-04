from userModel import User
from productModel import Product
from database import engine, session
from database import Base

Base.metadata.create_all(engine)

def create_user(name,age):
    user = User(name=name,age=age)
    session.add(user)
    session.commit()

def getAllUsers():   
    users = session.query(User).all()
    return users

def find_one_user(id):
    user = session.query(User).filter(User.id == id).first()
    return user

def update_user(id,name,age):
    user = find_one_user(id)
    user.name = name
    user.age = age
    session.commit()

def delete_user(id):
    user = find_one_user(id)
    session.delete(user)
    session.commit()

# create_user("Anna",20)

# all_users = getAllUsers()
# for user in all_users:
#     print(f"Name: {user.name}, Age: {user.age}")

# found_user = find_one_user(2)
# print(f"Name: {found_user.name}, Age: {found_user.age}")

# update_user(2,"Vardan",35)

# delete_user(2)