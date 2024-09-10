class Vehiculo:
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        
    def Ver(self):
        return f" [ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas} ]"
        
class Automovil(Vehiculo):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def Ver(self):
        return f" [ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas} ] [ Velocidad : { self.velocidad } km/hr ] [ Cilindrada : { self.cilindrada} cc ]"
    

class AutomovilPasajeros(Automovil):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ,numero_puestos:int):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos

    def Ver(self):
        return f" [ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas} ] [ Velocidad : { self.velocidad } kmh/hr ] [ Cilindrada : { self.cilindrada} cc ] [ Numero de Puestos : { self.numero_puestos} ]"

class AutomovilCarga(Automovil):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ,carga_kg:int):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.carga_kg = carga_kg
        
    def Ver(self):
        return f"[ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas}] [ Velocidad : { self.velocidad } km/hr ] [ Cilindrada : { self.cilindrada} cc ] [ Carga : { self.carga_kg} kg ] "
        
class Bicicleta(Vehiculo):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,tipo_bicicleta:str ) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo_bicicleta = tipo_bicicleta
        
    def Ver(self):
        return f"[ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas} ] [ Tipo Bicicleta : { self.tipo_bicicleta } ]"

class Motocicleta(Bicicleta):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,tipo_bicicleta:str ,nro_radios:int ,cuadro:str ,motor:str ):
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta )
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
        
    def Ver(self):
        return f"[ Marca : {self.marca} ] [ Modelo : { self.modelo} ] [ Numero de Ruedas : { self.numero_ruedas} ] [ Tipo Motocicleta : { self.tipo_bicicleta } ] [ Nro Radios : { self.nro_radios } ] [ Cuadro : { self.cuadro } ] [ Motor : { self.motor } ]"
        
    
    