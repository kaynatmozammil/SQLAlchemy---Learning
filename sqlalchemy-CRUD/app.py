from sqlalchemy.orm import sessionmaker

from model import User , engine 

Session = sessionmaker(bind = engine)

session = Session()

# user = User(name = "Kaynat Mozammil", age = 38)
# user_2 = User(name = "Faiz Khan" , age = 19)
# user_3 = User(name = "Abdullah Khan" , age = 23)
# user_4 = User(name = "Rayyan Khan" , age = 12)
# user_5 = User(name = "Rahmat Khan" , age = 19)
# # session.add(user)

# session.add(user_2)
# session.add_all([user_3,user_4 , user_5])

# session.commit()

# users = session.query(User).all()

# print(users[0].id)
# print(users[0].name)
# print(users[0].age)

# for user in users:
#     print(f"User id: {user.id}, name: {user.name}, age: {user.age}")


# user = session.query(User).filter_by(id = 1).one_or_none()
# user = session.query(User).filter_by(age = 19).first()
# print(user)
# print(user.id)
# print(user.name)
# print(user.age)

# user.name = "Faiz Mohammad"
# print(user.name)

# session.commit()

user = session.query(User).filter_by(id = 1).first()
print(user)
print(user.id)
print(user.name)
print(user.age)

session.delete(user)

print(user.name)

session.commit()
