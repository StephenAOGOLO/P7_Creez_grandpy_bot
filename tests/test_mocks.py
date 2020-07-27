from GrandPyBot import views, utils


def test_a01_home():
    def mock_home():
        return "<h1>Bonjour</h1>"
    views.home = mock_home
    result = views.home()
    assert result == "<h1>Bonjour</h1>"


def test_a02_home(monkeypatch):
    def mock_home():
        return "<h1>Bonjour</h1>"
    monkeypatch.setattr('GrandPyBot.views.home', mock_home)
    result = views.home()
    assert result == "<h1>Bonjour</h1>"


def test_a03_home():
    app = views.app
    client = app.test_client()
    url = '/'
    response = client.get(url)
    data = str(response.get_data().decode("utf-8"))
    print(">>>  "+data)
    assert "Stephen" in data
    assert response.status_code == 200


def test_b01_get_info_from_title(monkeypatch):
    def mock_get_info_from_title(__str__):
        return dict
    monkeypatch.setattr('GrandPyBot.utils.get_info_from_title', mock_get_info_from_title)
    result = utils.get_info_from_title("paris")
    assert result == dict


def test_c01_get_page_id_from_data(monkeypatch):
    def mock_get_page_id_from_data(__dict__):
        return int
    monkeypatch.setattr('GrandPyBot.utils.get_page_id_from_data', mock_get_page_id_from_data)
    var = dict()
    result = utils.get_page_id_from_data(var)
    assert result == int


def test_d01_get_article_wiki_by_pageid(monkeypatch):
    def mock_get_article_wiki_by_pageid(__int__):
        return str
    monkeypatch.setattr('GrandPyBot.utils.get_article_wiki_by_pageid', mock_get_article_wiki_by_pageid)
    result = utils.get_article_wiki_by_pageid(int)
    assert result == str


def test_e01_modelling_text(monkeypatch):
    def mock_modelling_text(__str__):
        pass
    pass
