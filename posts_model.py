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
                             thread_id VARCHAR(100),
                             user_id INTEGER,
                             file_path VARCHAR(100)
                             )''')
        cursor.close()
        self.connection.commit()
        
    def insert(self, thread_id, title, content, user, user_id, file_path):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO posts 
                          (thread_id, title, content, user, user_id, file_path) 
                          VALUES (?,?,?,?,?,?)''', (thread_id, title, content, user, str(user_id), file_path))
        cursor.close()
        self.connection.commit()
        
    def get(self, posts_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (str(posts_id),))
        row = cursor.fetchone()
        return row
     
    def get_all(self, thread_id, user_id = None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM posts WHERE user_id = ? AND thread_id = ?", ((str(user_id), thread_id,)))
        else:
            cursor.execute("SELECT * FROM posts WHERE thread_id = ?", (thread_id,),)
        rows = cursor.fetchall()
        return rows
    
    def delete(self, thread_id, posts_id, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM posts WHERE id = ? AND thread_id = ? AND user_id = ?''', (str(posts_id), thread_id, user_id),)
        cursor.close()
        self.connection.commit()    
        
        