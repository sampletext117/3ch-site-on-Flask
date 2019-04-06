from db import DB
from user_model import UserModel
from posts_model import PostModel


db_all = DB()
users_model = UserModel(db_all.get_connection())
users_model.init_table()
users_model.insert("test1", "111")
post_model = PostModel(db_all.get_connection())
post_model.init_table()
