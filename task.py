import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image
from size import size


def scale(toponym_longitude, toponym_lattitude, delta1, delta2):
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": "{0},pm2dgl".format(",".join([toponym_longitude, toponym_lattitude]))
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    # Создадим картинку
    # и тут же ее покажем встроенным просмотрщиком операционной системы
    Image.open(BytesIO(
        response.content)).show()


toponym_to_find = " ".join(sys.argv[1:])
toponym_longitude, toponym_lattitude, delta1, delta2 = list(size(toponym_to_find))
scale(toponym_longitude, toponym_lattitude, delta1, delta2)
