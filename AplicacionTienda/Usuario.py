class Usuario:

    def __init__(self,documento=None,nombre=None,telefono=None,valor=None):
        self.documento=documento
        self.nombre=nombre
        self.telefono=telefono
        self.valor=valor

    def __str__(self) -> str:
        datos="\n<<<<<<<<<<<<< DATOS CLIENTE >>>>>>>>>>>>>>>\n"
        datos+=f"Documento: {self.documento} , Nombre: {self.nombre}\n"
        datos+=f"Telefono: {self.telefono} , Valor:{self.valor}\n"

        return datos