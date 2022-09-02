from Usuario import *

class Almacenamiento:

    lista=[]
    listaGeneral=[]

    def registrar(self,cliente):
        
        self.lista.append(cliente)
        lista=[]
        lista.append(cliente.documento)
        lista.append(cliente.nombre)
        lista.append(cliente.telefono)
        lista.append(cliente.valor)

        print(lista)
        print(cliente)
        print(type(cliente))
        

        print(f"Cliente {cliente.nombre} registrado con exito!")
        return f"Cliente {cliente.nombre} registrado con exito!"

    def eliminar(self,documento):
        print(documento)
        cliente=self.consultarPorDocumento(documento)
        if(cliente!=None):
            nombre=cliente.nombre
            for i in range(len(self.listaGeneral)):
                lista=self.listaGeneral[i]
                print("-->",lista)
                if(cliente.documento==lista[0]):
                    print("Elimina")
                    self.listaGeneral.remove(lista)
                    self.lista.remove(cliente)
                    break
                mensaje=f"El cliente {nombre} se ha eliminado con exito!"
        
        return mensaje

    def actualizar(self,miCliente):
        cliente=self.consultarPorDocumento(miCliente.documento)
        mensaje=""
        if(cliente!=None):
            cliente.nombre=miCliente.nombre
            cliente.telefono=miCliente.telefono
            cliente.valor=miCliente.valor
            self.actualizarListaGeneral(cliente)
            mensaje="Se ha actualizado el cliente"
        else:
            mensaje="no se pudo actualizar"
        
            
        return mensaje

    def actualizarListaGeneral(self,cliente):
        for i in range(len(self.listaGeneral)):
            lista=self.listaGeneral[i]
            print("-->",lista)
            if(cliente.documento==lista[0]):
                print("Actualiza")
                lista[1]=cliente.nombre
                lista[2]=cliente.telefono
                lista[3]=cliente.valor
                
                break


    def obtenerLista(self):
        print(self.listaGeneral)
        return self.listaGeneral

    def consultarLista(self):
        if(self.validaTamanioLista()==True):
            for i in range(len(self.lista)):
                cliente=self.lista[i]
                print(cliente)
        
        return self.lista


    def consultarPorDocumento(self,documento):
        cliente=None 
        if(self.validaTamanioLista()==True):
            for est in self.lista:
                if(est.documento==documento):
                    cliente=est 
        
        return cliente
        

    def obtenerCantidads(self):
        return len(self.lista)

    
    def validaTamanioLista(self):
        if(len(self.lista)>0):
            return True
        else:
            print("\n<<<< No han registrado clientes >>>")
            return False
