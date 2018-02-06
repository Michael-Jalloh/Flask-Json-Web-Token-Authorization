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

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
            "username": x.username,
            "password": x.password
            }
        return {"users": list(map(lambda x: to_json(x), cls.select()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = 0
            for user in cls.select():
                num_rows_deleted +=user.delete_instance()

            return {"message":"{} row(s) deleted".format(num_rows_deleted)}
        except:
            return {"message":"Something went wrong"}

db.create_tables([User], safe=True)
