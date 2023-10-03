import pytest

@pytest.fixture
def user_credentials():
    email = "annlevina1111@mail.ru"
    password = "password123"
    return email, password