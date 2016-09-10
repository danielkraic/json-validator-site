import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../web'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import web
from nose.tools import *

def test_parse_ok():
    eq_(web.parse_json("{}"), "{}")
    eq_(web.parse_json("[]"), "[]")

@raises(ValueError)
def test_parse_failed_empty():
    web.parse_json("")

@raises(ValueError)
def test_parse_failed_wrong():
    web.parse_json("{1}")

@raises(ValueError)
def test_parse_failed_typo():
    web.parse_json("{\"a\":}")

def test_parse_root():
    app_tesing = web.app.test_client()
    res = app_tesing.get('/')
    assert not "Error" in res.get_data(as_text=True)
    assert not "JSON is valid" in res.get_data(as_text=True)

def test_parse_root_post_valid_object():
    app_tesing = web.app.test_client()
    res = app_tesing.post('/', data=dict(
        jsondata='{}'
    ))
    assert not "Error" in res.get_data(as_text=True)
    assert "JSON is valid" in res.get_data(as_text=True)

def test_parse_root_post_valid_array():
    app_tesing = web.app.test_client()
    res = app_tesing.post('/', data=dict(
        jsondata='[]'
    ))
    assert not "Error" in res.get_data(as_text=True)
    assert "JSON is valid" in res.get_data(as_text=True)
