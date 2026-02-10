import pytest
from src.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_creation():
    app = create_app()
    assert app is not None
    assert app.name == 'src.app'

def test_blueprint_registration(app):
    response = app.get('/')
    assert response.status_code == 200

def test_routes_blueprint_registered(app):
    from src.routes import main
    assert 'main' in create_app().blueprints
    assert main in create_app().blueprints.values()

def test_app_context(app):
    with app.application.app_context():
        assert True

def test_app_debug_mode():
    app = create_app()
    assert app.debug is True

def test_app_test_client(app):
    response = app.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data or b'Home' in response.data
