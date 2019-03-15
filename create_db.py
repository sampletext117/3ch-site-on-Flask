from db import DB
from user_model import UserModel
from posts_model import PostModel


db1 = DB('posts.db')
db2 = DB('users.db')
users_model = UserModel(db2.get_connection())
users_model.init_table()
users_model.insert("test1", "111")
post_model = PostModel(db1.get_connection())
post_model.init_table()
