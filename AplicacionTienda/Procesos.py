from Usuario import *
from Almacenamiento import *
from clases.operacionesMatematicas import *

class Procesos:
    productoGlobal=None
    miAlmacenamientoProductos=OperacionesMatematicas()

    usuarioGlobal=None
    miAlmacenamientoUsuarios=Almacenamiento()


    def llenarLista(self):
        miUsuario1 = Usuario("111","Santiago","3208798551","20000")
        miUsuario2 = Usuario("222","Felipe","321789","60000")
        
        print()
        self.miAlmacenamientoUsuarios.registrar(miUsuario1)
        self.miAlmacenamientoUsuarios.registrar(miUsuario2)


    def registrar(self,miUsuario):
        print("Cliente a registrar",miUsuario)
        return self.miAlmacenamientoUsuarios.registrar(miUsuario)

    def actualizar(self,miUsuario):
        return self.miAlmacenamientoUsuarios.actualizar(miUsuario)

    def eliminar(self,documento):
        return self.miAlmacenamientoUsuarios.eliminar(documento)


    def consultar(self,documento):
        usuario=self.miAlmacenamientoUsuarios.consultarPorDocumento(documento)

        if(usuario!=None):
            print(usuario)
        else:
            print(f"\nNo existe ningún cliente con el documento {documento}")
            
        return usuario

    def obtenerLista(self):
        lista=self.miAlmacenamientoUsuarios.obtenerLista()  
        return lista 
    
    def consultarLista(self):
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE CLIENTES ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamientoUsuarios.consultarLista()  
        print("\n*************************************************************\n")    
