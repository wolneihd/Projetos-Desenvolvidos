import sqlite3

class Funcs:
    def conecta_bd(self):
        self.conn = sqlite3.connect("users_db.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()  # Corrigido para fechar a conexão da instância atual

    def montaTabelas(self):
        self.conecta_bd()
        # CRIA TABELA DE USUARIOS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            );               
        """)
        self.conn.commit()
        self.desconecta_bd()
        print('Tabela criada com sucesso!')

    def insert_user(self, nome, idade):
        self.conecta_bd()  # Corrigido para chamar o método corretamente
        insert_sql = """INSERT INTO usuarios (nome, idade) VALUES (?, ?)"""
        self.cursor.execute(insert_sql, (nome, idade))
        self.conn.commit()
        self.desconecta_bd()
        return {'mensagem': 'Usuário inserido com sucesso!'}
    
    def get_all_user_database(self):
        self.conecta_bd() 
        dados = self.cursor.execute("""SELECT * FROM usuarios""")
        list_all_users = []
        for row in dados:
            id, nome, idade = row
            new_user = {'nome': nome, 'idade': idade, 'id_database': id}
            list_all_users.append(new_user)
        self.desconecta_bd()
        return list_all_users
    
    def delete_user(self, id):
        self.conecta_bd()
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao excluir o usuário: {e}")
            return {'erro': str(e)}
        finally:
            self.desconecta_bd()
        return {'ID excluído': id}
    
    def get_one_user(self, id):
        self.conecta_bd() 
        dados = self.cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        array_user = []
        for row in dados:
            id, nome, idade = row
            new_user = {'nome': nome, 'idade': idade, 'id_database': id}
        self.desconecta_bd()
        return new_user
    
    def update_one_user(self, id, nome, idade):
        self.conecta_bd()
        try:
            self.cursor.execute("UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?", (nome,idade,id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o usuário: {e}")
            return {'erro': str(e)}
        finally:
            self.desconecta_bd()
        return {'ID atualizado': id}