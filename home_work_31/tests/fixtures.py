from datetime import date, timedelta

import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = 'test'
    password = 'test'
    birth_date = date.today() - timedelta(days=5000)
    user = django_user_model.objects.create(
        username=username,
        password=password,
        birth_date=birth_date,
        role='admin'
    )
    print(user.username, user.password)
    response = client.post(
        '/user/token/', {
            'username': username,
            'password': password,
        },
        content_type='application/json',
    )
    return response.data['access']
