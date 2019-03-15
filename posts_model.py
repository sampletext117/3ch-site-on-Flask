class PostModel:
    def __init__(self, connection):
        self.connection = connection
        
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             title VARCHAR(100),
                             content VARCHAR(1000),
                             user VARCHAR(100),
                             user_id INTEGER
                             )''')
        cursor.close()
        self.connection.commit()
        
    def insert(self, title, content, user, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO posts 
                          (title, content, user, user_id) 
                          VALUES (?,?,?,?,?)''', (title, content, user, str(user_id)))
        cursor.close()
        self.connection.commit()
        
    def get(self, posts_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (str(posts_id),))
        row = cursor.fetchone()
        return row
     
    def get_all(self, user_id = None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM posts WHERE user_id = ?", (str(user_id),))
        else:
            cursor.execute("SELECT * FROM posts")
        rows = cursor.fetchall()
        return rows
    
    def delete(self, posts_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM posts WHERE id = ?''', (str(posts_id),))
        cursor.close()
        self.connection.commit()    
        
        