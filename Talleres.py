class vehiculo:
    #self: identifica variables
    def __init__(self, placa, modelo, marca):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca 
        self.velocidad = 0

    def acelerar (self):
        self.velocidad += 10

    def frenar (self):
        self.velocidad -=5
    
    def obtener_info(self):
    return ("El veichulo con placa: ", (self.placa), "del modelo : ", (self.modelo), "marca: ", (self.marca), "tuvo una velocidad de: ", (self.velocidad), 'km/h en la prueba')
    


    #casos de uso
    VehiculoC = vehiculo ('FME421', '2015','Audi')
    el_vehiculo.acelerar ()
    el_vehiculo.acelerar ()
    el_vehiculo.acelerar ()
    el_vehiculo.acelerar ()
    el_vehiculo.frena()
    print (el_vehiculo.obtener_info())