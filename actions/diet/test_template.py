from fastapi.testclient import TestClient

from actions.template.main import app

client = TestClient(app)


def test():
    assert True
