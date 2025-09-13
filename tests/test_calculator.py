from app.app import app as flask_app


# Tests for the Flask app routes.
def test_index_get():
    client = flask_app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Calculator" in r.data


# Test to check POST request handling.
def test_post_add():
    client = flask_app.test_client()
    r = client.post("/", data={"a": "2", "b": "3", "op": "add"})
    assert r.status_code == 200
    assert b"Result" in r.data
    assert b"5.0" in r.data or b"5" in r.data
