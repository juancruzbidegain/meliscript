#Importamos modulos necesarios

import requests
import logging

#Configuramos el modulo para el posterior use
logging.basicConfig(filename='scriptmeli.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

#Declaramos variables para que el script sea dinamico

seller_id = 179571326
site_id = "MLA"
url = f"https://api.mercadolibre.com/sites/{site_id}/search?seller_id={seller_id}"


#dejamos un array para ir guardando los items
productos = []



#Funcion para obtener los datos
def getData(url):
    response = requests.get(url)
    response = response.json()
    for product in response['results']:
        productos.append({"id": product['id'], "title": product['title'], "category_id" :product["category_id"], "price": product["price"]})

    createFile(productos)

#Funcion para crear el log
def createFile(info):
    for p in info:
        logging.info(f'El producto con id:{p["id"]} titulo: {p["title"]} categoria_id: {p["category_id"]} precio: {p["price"]}')



if __name__ == '__main__':
    getData(url)


