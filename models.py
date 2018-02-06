from peewee import *

db = SqliteDatabase('flask-rest.db')


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()
    password = CharField()

    @classmethod
    def get_user(cls,user):
        try:
            user = cls.get(username=user)
            return user
        except:
            return None

db.create_tables([User], safe=True)
