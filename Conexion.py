import mysql.connector

class DataBase:
    def __init__(self):
        self.conexion=mysql.connector.connect(
            user='root',
            password='12345', 
            host='localhost', 
            database='GAME'
        )
        self.cursor=self.conexion.cursor()
    def check_user(self, username, password):
        sql = f"SELECT * FROM users WHERE username= '{username}' AND password = '{password}' "
        try:
            self.cursor.execute(sql)
            user= self.cursor.fetchone()
            if user == None:
                return False
            else:
                return True
        except Exception as e:
            raise
        
    def into_user(self, username, password):
        if username=="" or password=="":
            return False
        else:
            sql = f"INSERT INTO users (id, username, password) VALUES (NULL, '{username}', '{password}')"
            try:
                self.cursor.execute(sql)
                self.conexion.commit()
                return True
            except Exception as e:
                return False
                raise
        
    def check_all(self,):
        sql = f"SELECT * FROM users"
        try:
            self.cursor.execute(sql)
            users=self.cursor.fetchall()
            return users
        except Exception as e:
            raise
    def delete_user(self, username):
        sql=f"DELETE FROM users WHERE username='{username}'"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            numero=self.cursor.rowcount
            return numero
        except Exception as e:
            return False
            raise
