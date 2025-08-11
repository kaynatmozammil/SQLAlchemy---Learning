import random 

from sqlalchemy.orm import sessionmaker

from model import User , engine

Session = sessionmaker(bind = engine)
session = Session()

name = ["Kaynat" , "Mozammil", "Adib" , "Danish"]
session = [20 , 21 , 22 ,23 ,24 , 26 , 24 ,56]

for i in range: 
    user = User(name = random.choice(name))
    age = User(name = random.choice(age))