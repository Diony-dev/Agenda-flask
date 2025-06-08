import sqlite3 as sql

class Contacto: # Una pequeña clase para representar un contacto, si no la tienes ya.
    def __init__(self, nombre, telefono, email, id=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class PyDB:
    def __init__(self, db_name):
        self.db_name = db_name
        # Abre la conexión. Es mejor que la conexión permanezca abierta
        # mientras el objeto PyDB esté en uso.
        self.conn = sql.connect(self.db_name)
        self.cursor = self.conn.cursor()
       
        self.create_database()  # Crea la tabla si no existe


    def create_database(self):
        # Este método ya no es necesario, ya que la tabla se crea en __init__
        # Pero lo dejo aquí por si quieres mantenerlo.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        self

    def insert_contact(self, contacto):
        self.cursor.execute('''
            INSERT INTO contactos (nombre, telefono, email)
            VALUES (?, ?, ?)
        ''', (contacto.nombre, contacto.telefono, contacto.email))
        self.conn.commit()
        # self.conn.close() # ¡ELIMINAR ESTA LÍNEA!

    def get_contacts(self):
        self.cursor.execute('SELECT * FROM contactos')
        rows = self.cursor.fetchall()
        contacts = []
        if rows:
         for row in rows:
            contacts.append({
                'id': row[0],
                'nombre': row[1],
                'telefono': row[2],
                'email': row[3]
            })
        # self.conn.close() # ¡ELIMINAR ESTA LÍNEA!
         return contacts
        else:
            return None  # Retorna None si no hay contactos

    def delete_contact(self, contact_id):
        self.cursor.execute('DELETE FROM contactos WHERE id = ?', (contact_id,))
        self.conn.commit()
        # self.conn.close() # ¡ELIMINAR ESTA LÍNEA!

    def update_contact(self, contact_id, contacto):
        self.cursor.execute('''
            UPDATE contactos
            SET nombre = ?, telefono = ?, email = ?
            WHERE id = ?
        ''', (contacto.nombre, contacto.telefono, contacto.email, contact_id))
        self.conn.commit()
        # self.conn.close() # ¡ELIMINAR ESTA LÍNEA!

    # --- RECOMENDACIÓN: Añadir un método para cerrar la conexión explícitamente ---
    def close(self):
        if self.conn: # Asegurarse de que la conexión existe antes de cerrarla
            self.conn.close()
            print(f"Conexión a {self.db_name} cerrada.")

    # --- RECOMENDACIÓN AVANZADA: Implementar el protocolo de gestor de contexto ---
    # Esto permite usar la clase con 'with' statement de forma más segura
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        print(f"Conexión a {self.db_name} cerrada automáticamente por 'with'.")

