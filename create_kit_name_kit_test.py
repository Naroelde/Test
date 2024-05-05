import requests
from sender_stand_request import post_new_client_kit, auth_token


# Тест создание нового пользователя и токена
def test_create_user():
    kit_body = {
        "firstName": "Irina",
        "email": "irina@mail.ru",
        "phone": "+74441237887",
        "comment": "Ребёнок спит, не шумите",
        "address": "г. Москва, ул. Хохотушкина, д. 16"
    }
    # Отправляется запрос на создание пользователя
    response = requests.post(
        "https://3e0a3adb-1ed2-4ee7-a2e8-791993c2d42a.serverhub.praktikum-services.ru/api/v1/users",
        json=kit_body).json()
    # Проверка, что токен создан
    assert response["authToken"]


# Тест создание набора
def test_create_user_kit():
    kit_body = {"name": "My kit"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Проверка, что код ответа 201
    assert response.status_code == 201


# Тест допустимое количество символов - 1
def test_quantity_of_symbols_one():
    kit_body = {"name": "a"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Проверка, что код ответа 201
    assert response.status_code == 201
    # Перевели переменную response в json формат, чтоб программа смогла прочитать ответ от сервера
    response = response.json()
    # Проверка, что в ответе поле name совпадает с полем name в запросе
    assert response["name"] == kit_body["name"]


# Тест допустимое количество символов (511)
def test_quantity_of_symbols_511():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест количество символов меньше допустимого (0):
def test_quantity_of_symbols_zero():
    kit_body = {"name": ""}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Здесь БАГ: сервер возвращает 201, а должен возвращать 400
    assert response.status_code == 400


# Тест количество символов больше допустимого (512)
def test_quantity_of_symbols_512():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Здесь БАГ: сервер возвращает 201, а должен возвращать 400
    assert response.status_code == 400


# Тест разрешены английские буквы
def test_english_letters():
    kit_body = {"name": "QWErty"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест разрешены русские буквы
def test_russian_letters():
    kit_body = {"name": "Мария"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест разрешены спецсимволы
def test_special_symbols():
    kit_body = {"name": "'№%@',"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест разрешены пробелы
def test_spaces():
    kit_body = {"name": " Человек и КО "}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест разрешены цифры
def test_string_123():
    kit_body = {"name": "123"}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response = response.json()
    assert response["name"] == kit_body["name"]


# Тест параметр не передан в запросе
def test_kit_body_not_sent():
    kit_body = {}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Здесь БАГ: сервер возвращает 500, а должен возвращать 400
    assert response.status_code == 400


# Тест передан другой тип параметра (число)
def test_numbers_123():
    kit_body = {"name": 123}
    # Отправляется запрос на создание набора
    response = post_new_client_kit(kit_body, auth_token)
    # Здесь БАГ: сервер возвращает 201, а должен возвращать 400
    assert response.status_code == 400
