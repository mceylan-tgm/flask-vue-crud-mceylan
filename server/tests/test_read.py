import os
import tempfile
from base64 import b64encode

import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_empty_db(client):
    """Start with a blank database."""

    valid_credentials = b64encode(b'mceylan:secret').decode('utf-8')
    headers = {'Authorization': 'Basic ' + valid_credentials}
    rv = client.get('/user', headers=headers)
    print(rv.status)
    assert rv.status_code == 200
