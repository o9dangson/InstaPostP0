import pytest

from app import App

# Set up
db = 'Database goes here'
@pytest.fixture
def app():
    app = App.app
    app.config.update({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# Routes
def test_home_get(client):
    response = client.get('/')
    assert response.status_code == 200

#@pytest.mark.parametrize("test_user", [
#    {'user':'Alex', 'pw': 'pw'},
#    {'user':'Bob', 'pw':'pass'}
#])
#def test_home_post(test_user, client):
#    data = {
#        "username":test_user['user'],
#        "password":test_user['pw']
#    }
#    response = client.post("/", data=data)
#    assert response.status_code == 200