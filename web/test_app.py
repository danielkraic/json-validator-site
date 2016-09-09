import app
from nose.tools import *

def test_parse_ok():
    eq_(app.parse_json("{}"), "{}")
    eq_(app.parse_json("[]"), "[]")

@raises(ValueError)
def test_parse_failed_empty():
    app.parse_json("")

@raises(ValueError)
def test_parse_failed_wrong():
    app.parse_json("{1}")

@raises(ValueError)
def test_parse_failed_typo():
    app.parse_json("{\"a\":}")

def test_parse_root():
    app_tesing = app.app.test_client()
    res = app_tesing.get('/')
    assert not "Error" in res.data 
    assert not "JSON is valid" in res.data

def test_parse_root_post_valid_object():
    app_tesing = app.app.test_client()
    res = app_tesing.post('/', data=dict(
        jsondata='{}'
    ))
    assert not "Error" in res.data 
    assert "JSON is valid" in res.data

def test_parse_root_post_valid_array():
    app_tesing = app.app.test_client()
    res = app_tesing.post('/', data=dict(
        jsondata='[]'
    ))
    assert not "Error" in res.data 
    assert "JSON is valid" in res.data

