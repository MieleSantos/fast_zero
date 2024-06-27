from sqlalchemy import select

from api.models import User


def test_creat_user(session):
    new_user = User(username="teste", password="teste", email="teste@teste.com")
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "teste"))
    assert user.username == "teste"
