# importando pymongo
import pymongo
# para que tome caracteres especiales y acentos
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

### Cadena de conexión de Mongo Atlas
MONGO_URL = "mongodb+srv://<username>:<password>@cluster0.xxxxxxx.mongodb.net/?retryWrites=true&w=majority"
MONGO_BASEDATOS = "database" # base de datos a utilizar
MONGO_COLECCION = "collection" # coleccion a utilizar
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

### Anticipando errores de ejecución usando 'TRY y EXCEPT'
try:
    ### Variable cliente que se va a conectar al cliente de Mongo
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    db = cliente[MONGO_BASEDATOS]
    coleccion = db[MONGO_COLECCION]
    
    coleccion.insert_many([
        {"nombre_estado": "Alabama", "anio": 2000, "cantidad": 3870598},
        {"nombre_estado": "Alabama", "anio": 2001, "cantidad": 3880476},
        {"nombre_estado": "Florida", "anio": 2000, "cantidad": 13237167},
        {"nombre_estado": "Florida", "anio": 2001, "cantidad": 13548077},
        {"nombre_estado": "Georgia", "anio": 2000, "cantidad": 7440877},
        {"nombre_estado": "Georgia", "anio": 2001, "cantidad": 7582146},
        {"nombre_estado": "South Carolina", "anio": 2000, "cantidad": 3535770},
        {"nombre_estado": "South Carolina", "anio": 2001, "cantidad": 3567172}
    ])
               
    cliente.close()
    
# Error por exceso de tiempo de respuesta    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")

# Error de conexión    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)