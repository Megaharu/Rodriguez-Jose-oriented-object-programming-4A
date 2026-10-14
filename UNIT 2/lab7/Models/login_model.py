from Controller.database_connection import Database_connection
class User:
    def __init__(self, username, password, db_config=None):
        self.username = username
        self.password = password
        self.db = Database_connection(db_config or {})

    def auth(self):
        query = "SELECT * FROM users WHERE username = %s AND password = %s" 

        result = self.db.ejecutar_consulta(query, (self.username, self.password))
        
        return result