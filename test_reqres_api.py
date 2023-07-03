from pprint import pprint
import requests

base_url = 'https://reqres.in/api/'
n = '\n'

def test_create_user_post():
    response = requests.post(
        url=f'{base_url}users/',
        json={
            "name": "Ivan",
            "job": "quality assurance"}
    )
    pprint(response.text)
    assert response.status_code == 201
    assert response.json()['name'] == "Ivan"
    assert response.json()['job'] == "quality assurance"


def test_update_user_put():
    response = requests.put(
        url=f'{base_url}users/490',
        json={
            "name": "Ivan",
            "job": "automation quality assurance"}
    )
    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == "Ivan"
    assert response.json()['job'] == "automation quality assurance"


def test_update_user_patch():
    response = requests.patch(
        url=f'{base_url}users/490',
        json={
            "name": "Ivan",
            "job": "SDET"}
    )
    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == "Ivan"
    assert response.json()['job'] == "SDET"


def test_user_delete():
    response = requests.delete(f'{base_url}users/490')

    pprint(response.text)
    assert response.status_code == 204


def test_user_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"

    response = requests.post(
        f'{base_url}register', json={"email": email, "password": password}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()["token"] == 'QpwL5tke4Pnpja7X4'


def test_register_user_unsuccessfull():
    response = requests.post(
        url=f'{base_url}register/',
        json={
            "email": "signacher@mail.ru"}
    )

    pprint(response.text)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_user_not_found():
    user_id = 20

    response = requests.get(f'{base_url}+users/{user_id}')

    pprint(response.text)
    assert response.status_code == 404


def test_user_id():
    user_id = 10

    response = requests.get(f'{base_url}users/{user_id}')

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id


def test_requested_page_number():
    page = 4

    response = requests.get(f'{base_url}users', params={'page': page})

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['page'] == page


def test_total_users():
    users_count = 12
    page = 4

    response = requests.get(f'{base_url}users', params={'page': page})

    pprint(response.text)
    assert response.json()['total'] == users_count
    assert response.status_code == 200

