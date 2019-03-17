from db import DB
from user_model import UserModel
from posts_model import PostModel


db_posts = DB('posts.db')
db_users = DB('users.db')
users_model = UserModel(db_users.get_connection())
users_model.init_table()
users_model.insert("test1", "111")
post_model = PostModel(db_posts.get_connection())
post_model.init_table()

