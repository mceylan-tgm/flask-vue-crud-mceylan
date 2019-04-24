import os
import json
from base64 import b64encode

import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


valid_credentials = b64encode(b'mceylan:secret').decode('utf-8')
headers = {'Authorization': 'Basic ' + valid_credentials, 'Content-Type': 'application/json', 'Accept': 'application/json'}


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/user', headers=headers)
    #print(rv.status)
    assert rv.status_code == 200

def test_create(client):
    rv = client.post('/user', headers=headers, data=dict(
        username="123",
        email="123@tgm.ac.at",
        image="ababababsb.jpg"
    ),)
    print(rv.status)
    assert b'success' in rv.data