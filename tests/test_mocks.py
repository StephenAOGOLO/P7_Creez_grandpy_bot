import GrandPyBot as Gpb
from GrandPyBot.views import home, sender
from GrandPyBot import templates
from GrandPyBot import views, utils
from flask import request, jsonify, render_template
import requests
import json


def test_home_01():
    def mock_home():
        return "<h1>Bonjour</h1>"
    views.home = mock_home
    result = views.home()
    assert result == "<h1>Bonjour</h1>"


def test_home_02(monkeypatch):
    def mock_home():
        return "<h1>Bonjour</h1>"
    monkeypatch.setattr('GrandPyBot.views.home', mock_home)
    result = views.home()
    assert result == "<h1>Bonjour</h1>"


def test_home_03():
    app = views.app
    client = app.test_client()
    url = '/'
    response = client.get(url)
    data = str(response.get_data().decode("utf-8"))
    print(">>>  "+data)
    assert "Stephen" in data
    assert response.status_code == 200


def test_get_info_from_title_01(monkeypatch):
    def mock_get_info_from_title(one_word_or_sentence):
        return dict
    monkeypatch.setattr('GrandPyBot.utils.get_info_from_title', mock_get_info_from_title)
    result = utils.get_info_from_title("paris")
    assert result == dict


def test_get_page_id_from_data_01(monkeypatch):
    def mock_get_page_id_from_data(__dict__):
        return int
    monkeypatch.setattr('GrandPyBot.utils.get_page_id_from_data', mock_get_page_id_from_data)
    var = dict()
    result = utils.get_page_id_from_data(var)
    assert result == int


def test_get_article_wiki_by_pageid_01(monkeypatch):
    def mock_get_article_wiki_by_pageid(__int__):
        return str
    monkeypatch.setattr('GrandPyBot.utils.get_article_wiki_by_pageid', mock_get_article_wiki_by_pageid)
    result = utils.get_article_wiki_by_pageid(int)
    assert result == str


