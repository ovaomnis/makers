import datetime

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

"""
SQLAlchemy -> package to work with DB
"""

"""
SLQAlchemy ORM (Object Related Mapping) -> allows to work with db using OOP. Create table and relation
using Python classes. Represents system to create Queries using OOP instead SQL 
"""

db = 'postgresql://postgres:adenloves@localhost:5432/sqlalchemy_orm'
engine = create_engine(db, echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    username = Column(String(50),
                      nullable=False,
                      unique=True)
    email = Column(String(80),
                   nullable=False)
    password = Column(String(100),
                      nullable=False)
    posts = relationship('Post', backref='author')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer,
                     ForeignKey('users.id'))

    def __str__(self):
        return self.title

    # __tableargs__ = (
    #     PrimaryKeyConstraint('id', name='post_pk')
    # )


# Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

# user1 = User(username='john',
#              email='johnShow@gmail.com',
#              password='test1234')
# user2 = User(username='sam',
#              email='samSmith@gmail.com',
#              password='test1234')
#
# post1 = Post(
#     title='First Post',
#     body='test',
#     user_id=1
# )
# post2 = Post(
#     title='Second Post',
#     body='test',
#     user_id=2
# )
# post3 = Post(
#     title='Third Post',
#     body='test',
#     user_id=2
# )
#
# session.add_all([post1, post2, post3])
# print(session.new)
# session.commit()

""" Selecting """

# for post in session.query(Post).all():
#     print(post.title)

# post_count = session.query(Post).count()
# print(post_count)

# first_post = session.query(Post).first()
# print(first_post.title)

# print(session.query(Post).filter(Post.title=='First Post').all())

# print(session.query(Post).limit(2).offset(2).all())

# post = session.query(Post).filter(Post.id=='2').all()
# print(post[0].title)

""" Updating """

# session.query(Post).filter(Post.title.ilike('%Post%')).update({'body': 'new updated'})
# session.commit()

""" Deleting """
# session.query(Post).filter(Post.id=='3').delete()
# session.commit()
