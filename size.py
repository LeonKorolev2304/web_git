import requests


def size(toponym_to_find):
    # Пусть наше приложение предполагает запуск:
    # python search.py Москва, ул. Ак. Королева, 12
    # Тогда запрос к геокодеру формируется следующим образом:

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    with open('res.json', 'w', encoding='utf8') as f:
        print(json_response, file=f)
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    envelope_longitude, envelope_lattitude = toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" ")
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    delta1 = str(2 * abs(float(toponym_longitude) - float(envelope_longitude)))
    delta2 = str(2 * abs(float(toponym_lattitude) - float(envelope_lattitude)))
    return toponym_longitude, toponym_lattitude, delta1, delta2

