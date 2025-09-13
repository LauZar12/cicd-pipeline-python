"""Unit tests."""

from app.app import app as flask_app


def test_index_get():
    """Test that GET request to '/' returns status 200."""
    client = flask_app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Calculator" in r.data


def test_post_add():
    """Test that POST request with addition returns correct result."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "2", "b": "3", "op": "add"})
    assert r.status_code == 200
    assert b"Result" in r.data
    assert b"5" in r.data


def test_post_subtract():
    """Test subtraction."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "5", "b": "3", "op": "subtract"})
    assert r.status_code == 200
    assert b"2" in r.data


def test_post_multiply():
    """Test multiplication."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "4", "b": "3", "op": "multiply"})
    assert r.status_code == 200
    assert b"12" in r.data


def test_post_divide():
    """Test division."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "10", "b": "2", "op": "divide"})
    assert r.status_code == 200
    assert b"5" in r.data


def test_post_invalid_input():
    """Test error handling when input is not numeric."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "abc", "b": "2", "op": "add"})
    assert r.status_code == 200
    assert b"Invalid input" in r.data


def test_post_invalid_operation():
    """Test error handling for an invalid operation."""
    client = flask_app.test_client()
    r = client.post("/", data={"a": "2", "b": "2", "op": "unknown"})
    assert r.status_code == 200
    assert b"Invalid operation" in r.data
