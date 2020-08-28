from GrandPyBot import views, utils
from GrandPyBot.utils import Loading
import requests
import json


"""
def test_f(monkeypatch):
    def mock_f():
        return 1
    monkeypatch.setattr('package.f', mock_f)
    result = package.f()
    assert result == 1
"""

""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""
""" Start of test for is_entry_empty() """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_is_entry_empty_01(monkeypatch):
    def mock_is_entry_empty(mot):
        return {"status": False, "text": "brésil"}
    monkeypatch.setattr("GrandPyBot.utils.is_entry_empty", mock_is_entry_empty)
    result = utils.is_entry_empty(" brésil ")
    assert type(result) == dict


def test_is_entry_empty_02(monkeypatch):
    def mock_is_entry_empty(mot):
        return {"status": False, "text": "brésil"}
    monkeypatch.setattr("GrandPyBot.utils.is_entry_empty", mock_is_entry_empty)
    result = utils.is_entry_empty(" brésil ")
    assert result == {"status": False, "text": "brésil"}


def test_is_entry_empty_03(monkeypatch):
    def mock_is_entry_empty(mot):
        return {"status": True, "text": "Aucun texte"}
    monkeypatch.setattr("GrandPyBot.utils.is_entry_empty", mock_is_entry_empty)
    result = utils.is_entry_empty("    ")
    assert result == {"status": True, "text": "Aucun texte"}


""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""
""" End of test for is_entry_empty() """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"""     Start of test for home()       """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


#def test_home_01(monkeypatch):
#    def mock_home():
#        return "<h1>test page</h1>"
#    monkeypatch.setattr('GrandPyBot.views.home', mock_home)
#    result = views.home()
#    assert type(result) == type(render_template)


""""""""""""""""""""""""""""""""""""""""""
"""     End of test for home()         """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"""Start of test for entry_treatment()"""
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_entry_treatment(monkeypatch):
    def mock_entry_treatment(text):
        return "http://test/api/search="+text
    monkeypatch.setattr('GrandPyBot.utils.entry_treatment', mock_entry_treatment)
    result = utils.entry_treatment("brésil")
    assert result == "http://test/api/search=brésil"


""""""""""""""""""""""""""""""""""""""""""
"""     End of test for home()         """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"""Start of test for cleanup_text()"""
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_cleanup_text(monkeypatch):
    def mock_cleanup_text(text):
        return text
    monkeypatch.setattr('GrandPyBot.utils.cleanup_text', mock_cleanup_text)
    result = utils.cleanup_text("brésil")
    assert result == "brésil"


""""""""""""""""""""""""""""""""""""""""""
"""     End of test for cleanup_text() """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"Start of test for get_info_from_title() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_get_info_from_title(monkeypatch):
    def mock_get_info_from_title(text):
        snippet = 'homonymes, voir <span class="searchmatch">Brésil</span>' \
                  ' (bois) et Marguerite <span class="searchmatch">Brésil</span>.' \
                  ' République fédérative du <span class="searchmatch">Brésil</span>' \
                  ' (pt)\xa0República Federativa do Brasil\xa0Écouter Le ' \
                  '<span class="searchmatch">Brésil</span> (en portugais\xa0:\xa0Brasil'
        return {0: {'ns': 0,
                 'title': 'Brésil',
                 'pageid': 398,
                 'size': 326750,
                 'wordcount': 34391,
                 'snippet': snippet,
                 'timestamp': '2020-07-26T22:40:32Z'}
                }
    monkeypatch.setattr('GrandPyBot.utils.Loading.get_info_from_title', mock_get_info_from_title)
    result = Loading.get_info_from_title("brésil")
    assert result[0]["title"] == "Brésil"


""""""""""""""""""""""""""""""""""""""""""
" End of test for get_info_from_title()  "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Start of test for get_page_id_from_data()      """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_get_page_id_from_data(monkeypatch):
    def mock_get_page_id_from_data(text):
        snippet = 'homonymes, voir <span class="searchmatch">Brésil</span>' \
                  ' (bois) et Marguerite <span class="searchmatch">Brésil</span>.' \
                  ' République fédérative du <span class="searchmatch">Brésil</span>' \
                  ' (pt)\xa0República Federativa do Brasil\xa0Écouter Le ' \
                  '<span class="searchmatch">Brésil</span> (en portugais\xa0:\xa0Brasil'
        return {0: {'ns': 0,
                 'title': 'Brésil',
                 'pageid': 398,
                 'size': 326750,
                 'wordcount': 34391,
                 'snippet': snippet,
                 'timestamp': '2020-07-26T22:40:32Z'}
                }
    monkeypatch.setattr('GrandPyBot.utils.get_page_id_from_data', mock_get_page_id_from_data)
    result = utils.get_page_id_from_data("brésil")
    assert result[0]["pageid"] == 398


""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for get_page_id_from_data() """
""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""
"Start of test for get_article_wiki_by_pageid() "
""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""


def test_get_article_wiki_by_pageid(monkeypatch):
    def mock_get_article_wiki_by_pageid():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.Loading.get_article_wiki_by_pageid', mock_get_article_wiki_by_pageid)
    result = utils.Loading.get_article_wiki_by_pageid()
    assert result == 1


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for get_article_wiki_by_pageid() """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""
"          Start of test for hash_text()             "
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_hash_text(monkeypatch):
    def mock_hash_text(text):
        return str(text).split()
    monkeypatch.setattr('GrandPyBot.utils.hash_text', mock_hash_text)
    result = utils.hash_text("aah ohh brésil de fre")
    assert result == ["aah", "ohh", "brésil", "de", "fre"]


""""""""""""""""""""""""""""""""""""""""""
"""     End of test for hash_text() """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"Start of test for word_bad() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_is_word_bad(monkeypatch):
    def mock_is_word_bad(liste_1, liste_2):
        return list(set(liste_1).difference(liste_2))
    monkeypatch.setattr('GrandPyBot.utils.is_word_bad', mock_is_word_bad)
    liste_1 = ["a", "b", "c", "d"]
    liste_2 = {"1": ["a", "b", "d"]}
    result = utils.is_word_bad(liste_1, liste_2["1"])
    assert result == ["c"]


""""""""""""""""""""""""""""""""""""""""""
"""     End of test for word_bad() """
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""
"Start of test for stop_words_with_json() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_stop_words_with_json(monkeypatch):
    def mock_stop_words_with_json():
        return True
    monkeypatch.setattr('GrandPyBot.utils.Loading.stop_words_with_json', mock_stop_words_with_json)
    result = utils.Loading.stop_words_with_json()
    result = result["6"]
    test_word = "hasard"
    assert test_word == result


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for stop_words_with_json() """
""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""
"Start of test for get_coordinates_from_osm() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_get_coordinates_from_osm(monkeypatch):
    def mock_get_coordinates_from_osm():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.Loading.stop_words_with_json', mock_get_coordinates_from_osm)
    test_load = Loading()
    result = utils.Loading.get_coordinates_from_osm(test_load, "openclassrooms")
    assert result["all"]["geojson"]["coordinates"] == [2.3504885, 48.8747786]


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for get_coordinates_from_osm() """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""
"Start of test for get_coordinates_from_wiki() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_get_coordinates_from_wiki(monkeypatch):
    def mock_get_coordinates_from_wiki():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.Loading.stop_words_with_json', mock_get_coordinates_from_wiki)
    test_load = Loading()
    result = utils.Loading.get_coordinates_from_wiki(test_load, "carnon")
    assert result["30323"]["coordinates"] == [{'globe': 'earth', 'lat': 43.546857, 'lon': 3.979254, 'primary': ''}]


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for get_coordinates_from_wiki() """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""
"Start of test for gpb_messages() "
""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""


def test_gpb_messages(monkeypatch):
    def mock_gpb_messages():
        return 1
    monkeypatch.setattr('GrandPyBot.utils.Loading.stop_words_with_json', mock_gpb_messages)
    test_load = Loading()
    test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                " Sed non risus. Suspendisse lectus tortor, dignissim sit amet," \
                " adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam."
    result = utils.Loading.gpb_messages(test_load, "carnon", test_text)
    assert "carnon" in result.lower()


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""     End of test for gpb_messages() """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""