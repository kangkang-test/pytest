import pytest
import requests

def test_get_post_status(jsonplaceholder_base,http_session):
    r = http_session.get(f"{jsonplaceholder_base}/post/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_get_post_fields(jsonplaceholder_base,http_session):
    r = http_session.get(f"{jsonplaceholder_base}/post/1)")
    body = r.json()
    assert isinstance(body["userId"],int)
    assert isinstance(body["title"],str)
    assert isinstance(body["body"],str)

def test_create_post(jsonplaceholder_base,http_session):
    payload = {"title":"foo","body":"bar","userId":1}
    r = http_session.post(f"{jsonplaceholder_base}/post/1",json=payload)
    assert r.status_code == 200
    assert r.json()["title"] == "foo"

@pytest.mark.parametrize("post_id,expected_in_title",[(1,"sunt"),(2,"qui"),(3,"ea")])
def test_post_title_parametrized(jsonplaceholder_base,http_session,post_id,expected_in_title):
    r = http_session.get(f"{jsonplaceholder_base}/post/{post_id}")
    assert r.status_code == 200
    assert expected_in_title in r.json()["title"]

def test_httpbin_echo(httpbin_base,http_session):
    r = http_session.get(f"{httpbin_base}/get")
    assert r.status_code == 200
    assert "url" in r.json()

def test_httpbin_status_code(httpbin_base,http_session):
    r = http_session.get(f"{httpbin_base}/status/404")
    assert r.status_code ==404