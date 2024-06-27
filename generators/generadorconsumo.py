import random
def generarDatos():   
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellin","Cali","Bogota","Cartagena","Barranquilla"])
        responsable=random.choice(["Estefa Zapata","Jaime Arenas","Maria Zapata","Juan Gallego","Laura Masmela"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())