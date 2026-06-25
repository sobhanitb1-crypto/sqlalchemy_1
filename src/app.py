from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine('sqlite:///school.db')
engine.connect()

Base = declarative_base()

class User(Base):
    
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    filed = Column(String)
    gpa = Column(Float)
    
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionlocal = session()


# user1 = User(name = "ALi", filed="Computer", gpa = 17.36)
# user2 = User(name = "Saeed", filed = "IT", gpa = 16.32)
# user3 = User(name = "Nima", filed = "Sofware", gpa = 18.08)
# # sessionlocal.add(user1)
# # sessionlocal.add(user2)
# sessionlocal.add(user3)
# sessionlocal.commit()
##################################################################


# user_lists = sessionlocal.query(User).all()
# print(user_lists)
# for user in user_lists:
#     print(user.name)
#     print(user.filed)
#     print(user.gpa)
#     print("_"*30)

# user_by_id = sessionlocal.query(User).filter_by(id = 2).first()
# print(user_by_id.filed, user_by_id.name)

# temp = sessionlocal.query(User).filter(User.name == "Nima").all()
# print(temp)

# temp2 = sessionlocal.query(User).filter(User.name.like("%N%")).all()
# print(temp2)

# user = sessionlocal.query(User).filter_by(id = 1).first()
# if user != None:
#     sessionlocal.delete(User)
#     sessionlocal.commit()
    
# else:
#     print("Your ID does not exist")
    
# user = sessionlocal.query(User).filter_by(name = "Nima").first()
# user.gpa = 19.36
# user.name = "Ahmad"
# user.filed = "Network"
# sessionlocal.commit()

class Teacher(Base):
    
    __tablename__ = "Teachers"
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    personelid = Column(String)
    salary = Column(Float)
    
Base.metadata.create_all(engine)

# session = sessionmaker(bind=engine)
# sessionlocal = session()