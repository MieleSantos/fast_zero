from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from api.app import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_root_deve_retornar_ok_e_ola_mundo_html(client):
    response = client.get("/html")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert


def test_create_user(client):
    response = client.post(  # UserShema
        "/users/",
        json={
            "username": "string",
            "password": "senha",
            "email": "user@example.com",
        },
    )
    # Voltou 201?
    assert response.status_code == HTTPStatus.CREATED

    # validar UserPublic
    assert response.json() == {
        "id": 1,
        "username": "string",
        "email": "user@example.com",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {"id": 1, "username": "string", "email": "user@example.com"},
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "string",
            "email": "user@example.com",
            "password": "senha",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "string",
        "email": "user@example.com",
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
