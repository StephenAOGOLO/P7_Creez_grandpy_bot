from GrandPyBot.views import home, sender
from GrandPyBot import templates
from GrandPyBot import views
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


def test_sender_01():
    def mock_sender():
        return jsonify(["ok"])
    views.sender = mock_sender
    result = views.sender()
    assert result == jsonify(["ok"])



