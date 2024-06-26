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


def test_create_user(client):

    response = client.post(  # UserShema
        "/users/",
        json={
            "username": "teste1",
            "password": "senha",
            "email": "test@teste.com",
        },
    )
    # Voltou 201?
    assert response.status_code == HTTPStatus.CREATED

    # validar UserPublic,
    assert response.json() == {
        "username": "teste1",
        "id": 1,
        "email": "test@teste.com",
    }


def test_root_deve_retornar_ok_e_ola_mundo_html(client):

    response = client.get("/html")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
