from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, TodoList
from random import randint
import string

def users(count=10):
    fake = Faker()
    while i < count:
        u = User(username=fake.user_name(),
                 email = fake.email(),
                 password='password',
                 member_since=fake.past_date(),
                 last_seen=fake.past_date(),
                 is_admin = True)                 
        db.session.add(u)

        # trying to commit data, but if it is a duplicate then it rollbacks
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def todolists(count = 75):
    fake = Faker()

    # checking how many users are in the table
    user_count = User.query.count()
    for i in range(count):
        # offset dicards a certain number of results, n is a random number between 0 and then user_count -1
        # so it is picking a random user and don't care about duplicated users because users can have multiple compositions
        u = User.query.offset(randint(0, user_count - 1)).first()
        c = TodoList(title = string.capwords(fake.bs()),
                    create_at = fake.past_date(), 
                    creator = u)
        db.session.add(c)
    db.session.commit()

def todos(count = randint(5,75)):
    fake = Faker()
    Todo(description = , 
        created_at = fake.past_data(),
        finished_at= fake.past_data(), 
        is_finished= , 
        creator= u, 
        todolist_id=)

        # how to get 5 to 75 tasks per list?