from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    

Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)
session = Session()


new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

new_user = User(name="Bob", age=25)
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.name, user.age)
    
    
    
print('실행완료')