from CURD import Database, Model, Field, PrimaryKey, ForeignKey, Sugar


class User(Model):
    name = Field()
    email = Field()


class Post(Model):
    name = Field()
    post_id = PrimaryKey()
    user_id = ForeignKey(User.id)

# configure Database
Database.config(db="mydb", user="root", passwd="")
