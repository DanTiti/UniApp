import sqlite3

class bd:
    def __init__(self, bdName="Mascotas.db"):
        self.conn = None
        try:
            self.conector = sqlite3.connect(bdName)
            self.Tables()
        except KeyError as e:
            print(f"Error al conectar con SQLite: {e}")
        
    def Tables(self):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mascotas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    mascota TEXT NOT NULL,
                    contacto TEXT,
                    vacunas TEXT,
                    alergias TEXT,
                    padecimientos TEXT,
                    img TEXT
                );
            """)

            self.conector.commit()
        except KeyError as e:
            print(f"Error al crear las tablas: {e}")

    def AgregarUsuario(self, user, password):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                INSERT INTO usuario (username, password)
                VALUES (?, ?);
            """, (user, password))
            self.conector.commit()
            print("Se ha agregado el usuario exitosamente")
        except:
            pass

    def AgregarMascota(self, nombreD, nombreM, contacto, vacunas, alergias, padecimientos, img):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                INSERT INTO mascotas (nombre, mascota, contacto, vacunas, alergias, padecimientos, img)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (nombreD, nombreM, contacto, vacunas, alergias, padecimientos, img))
            self.conector.commit()
            print("Mascota agregada exitosamente.")
        except KeyError as e:
            print(f"Error al conectar con SQLite: {e}")
            
    def ObtenerInfoMascotas(self):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                SELECT * FROM mascotas;
            """)
            data = cursor.fetchall()
            self.conector.commit()
            print("Se ha obtenido la informacion correctamente")
            return data
        except:
            pass
        
        
    def obtener_info_derecha(self):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                SELECT id, nombre, mascota, contacto FROM mascotas;
            """)
            data = cursor.fetchall()
            self.conector.commit()
            print("Se ha obtenido la informacion correctamente")
            return data
        except:
            pass
        
    def Obtener_info_lista(self):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                SELECT id, img, nombre, mascota FROM mascotas;
            """)
            data = cursor.fetchall()
            self.conector.commit()
            print("Se ha obtenido la informacion correctamente")
            return data
        except:
            pass
        

    def ObtenerInfo(self, id):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                SELECT * FROM mascotas WHERE id = ?;
            """, id)
            self.conector.commit()
            print("Se ha encontrado correctamente")
        except:
            pass

    def EliminarRegistro(self, id):
        try:
            cursor = self.conector.cursor()
            cursor.execute("""
                DELETE FROM mascotas WHERE id = ?;
            """, id)
            self.conector.commit()
            print("Se ha eliminado el registro")
        except:
            pass

    def EditarInfo(self):
        pass

    def Cerrar(self):
        if self.conector:
            self.conector.close()
            print("La conexion se ha cerrado")

