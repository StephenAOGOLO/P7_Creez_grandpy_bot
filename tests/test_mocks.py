from GrandPyBot import views, utils
from flask import render_template


"""
def test_f(monkeypatch):
    def mock_f():
        return 1
    monkeypatch.setattr('package.f', mock_f)
    result = package.f()
    assert result == 1
"""


#def is_entry_empty(text):
#    status = False
#    text = text.strip()
#    if text == "":
#        status = True
#        text = "Pouvez-vous reformuler votre question !"
#    report = {"status": status, "text": text}
#    return report


def test_is_entry_empty_01(monkeypatch):
    def mock_is_entry_empty(mot):
        return {"status": bool, "text": str}
    monkeypatch.setattr("GrandPyBot.utils.is_entry_empty", mock_is_entry_empty)
    result = utils.is_entry_empty(" brésil ")
    assert result == {"status": False, "text": "brésil"}


def test_is_entry_empty_02(monkeypatch):
    def mock_is_entry_empty(mot):
        return {"status": bool, "text": str}
    monkeypatch.setattr("GrandPyBot.utils.is_entry_empty", mock_is_entry_empty)
    result = utils.is_entry_empty("    ")
    assert result == {"status": False, "text": "brésil"}


def test_home(monkeypatch):
    def mock_home():
        return 1
    monkeypatch.setattr('GrandPyBot.views.home', mock_home)
    result = views.home()
    assert result == 1


#def test_is_entry_empty(monkeypatch):
#    def mock_is_entry_empty():
#        return 1
#    monkeypatch.setattr('GrandPyBot.utils.is_entry_empty', mock_is_entry_empty)
#    result = utils.is_entry_empty()
#    assert result == 1


def test_entry_treatment(monkeypatch):
    def mock_entry_treatment():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.entry_treatment', mock_entry_treatment)
    result = utils.entry_treatment()
    assert result == 1


def test_cleanup_text(monkeypatch):
    def mock_cleanup_text():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.cleanup_text', mock_cleanup_text)
    result = utils.cleanup_text()
    assert result == 1


def test_get_info_from_title(monkeypatch):
    def mock_get_info_from_title():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.get_info_from_title', mock_get_info_from_title)
    result = utils.get_info_from_title()
    assert result == 1


def test_get_page_id_from_data(monkeypatch):
    def mock_get_page_id_from_data():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.get_page_id_from_data', mock_get_page_id_from_data)
    result = utils.get_page_id_from_data()
    assert result == 1


def test_get_article_wiki_by_pageid(monkeypatch):
    def mock_get_article_wiki_by_pageid():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.get_article_wiki_by_pageid', mock_get_article_wiki_by_pageid)
    result = utils.get_article_wiki_by_pageid()
    assert result == 1


def test_hash_text(monkeypatch):
    def mock_hash_text():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.hash_text', mock_hash_text)
    result = utils.hash_text()
    assert result == 1


def test_is_word_bad(monkeypatch):
    def mock_is_word_bad():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.is_word_bad', mock_is_word_bad)
    result = utils.is_word_bad()
    assert result == 1


def test_stop_words_with_json(monkeypatch):
    def mock_stop_words_with_json():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.stop_words_with_json', mock_stop_words_with_json)
    result = utils.stop_words_with_json()
    assert result == 1

