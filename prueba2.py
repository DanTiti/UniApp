from bd import bd as base

class verinfo():
    def veriingo(self):
        # Crear una instancia de la clase bd
        base_instancia = base()

        # Llamar al método ObtenerInfoMascotas usando la instancia
        self.data = base_instancia.ObtenerInfoMascotas()
        
        # Imprimir los datos
        print(self.data)

        # Cerrar la conexión de la base de datos después de la consulta
        base_instancia.Cerrar()
