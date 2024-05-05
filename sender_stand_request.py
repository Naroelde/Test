import pytest
import requests
from configuration import BASE_URL, CREATE_NEW_USER


# Функция генерации нового токена
@pytest.fixture()
def auth_token():
    kit_body = {
        "firstName": "Ирина",
        "email": "irina@mail.ru",
        "phone": "+74441237887",
        "comment": "Ребёнок спит, не шумите",
        "address": "г. Москва, ул. Хохотушкина, д. 16"
    }
    # Запрос на создание нового пользователя
    response = requests.post(
        f"{BASE_URL}+{CREATE_NEW_USER}",
        json=kit_body).json()
    # Возвращается новый токен и его можно дальше использовать в тестах
    return response["authToken"]


# Функция создания нового набора
def post_new_client_kit(kit_body, auth_token):
    # Отправляется запрос на создание набора
    response = requests.post(
        f'https://3e0a3adb-1ed2-4ee7-a2e8-791993c2d42a.serverhub.praktikum-services.ru/api/v1/kits',
        json=kit_body,
        headers={"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
    )
    return response
