import requests as rqsts
import logging as lg
lg.basicConfig(level=lg.INFO)


def transform_to_upper(text):
    return {"text-original": text, "text-transformed": text.upper()}


def text_parser(text, sep=" "):
    data = text["text-transformed"]
    data = data.split(sep)
    text["text-transformed"] = data
    return text


def data_replace(text, sep="+"):
    data = text["text-transformed"]
    data = data.replace(' ', sep)
    text["text-transformed"] = data
    return text


def text_replace(text, sep="+"):
    text = text.replace(' ', sep)
    return text


def text_result(text):
    return text["text-transformed"]


def data_from_wiki(text):
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exchars=175&format=json&titles='
    url = wikiUrl+text
    data_raw = rqsts.get(url)
    lg.warning(">> 1 - type: {}\n".format(type(data_raw)))
    lg.warning(">> 1 - valeur: {}\n".format(data_raw))
    data_json = data_raw.json()
    lg.warning(">> 2 - type: {}\n".format(type(data_json)))
    lg.warning(">> 2 - valeur: {}\n".format(data_json))
    browse_data(data_json)
    lg.warning(">> 4 - type: {}\n".format(type(data_json[1][1])))
    return data_json[1][1]


def browse_data(data):
    lg.warning("Le type de cette donnée est: {}\n".format(type(data)))
    for e in data:
        print(e)
    lg.warning("\n")
    lg.warning(">> 3 - type: {}\n".format(type(data[1][1])))
    lg.warning(data[1][1])
    lg.warning("\n")


def start_wiki():
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=opensearch&format=json&search=francais'
    data_raw = rqsts.get(wikiUrl)
    data_json = data_raw.json()
    return data_json[1][1]


def get_info_from_title(title):
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch='
    url = wikiUrl + str(title)
    all_data = rqsts.get(url)
    all_data = all_data.json()
    all_data = all_data["query"]["search"]
    list_data = all_data
    dict_data = {}
    for i, e in enumerate(list_data):
        dict_data[i] = e
    print("\n")
    print("Voici le contenu du dictionnaire :")
    print("\n")
    for k, v in dict_data.items():
        print("{} ----> {}".format(k, v))
    return dict_data


def get_page_id_from_data(all_data):
    return all_data[0]["pageid"]


def get_article_wiki_by_pageid(page_id):
    """ paris = pageids=681159"""
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exsentences=2&explaintext=true&pageids='
    page_id = str(page_id)
    url = wikiUrl+page_id
    data_raw = rqsts.get(url)
    print(">> 1.1 - type: {}\n".format(type(data_raw)))
    print(">> 1.1 - valeur: {}\n".format(data_raw))
    dict_data = data_raw
    print(">> 2.1 - type: {}\n".format(type(dict_data)))
    print(">> 2.1 - valeur: {}\n".format(dict_data))
    data = dict_data.json()
    print(">> 3.1 - valeur: {}\n".format(data))
    return data["query"]["pages"][page_id]["extract"]


def modelling_text(text):
    pass


def is_country_known(text):
    status = False
    country = ""

    list_contry = ["France", "Espagne", "Etats-Unis", "Chine", "Italie", "Royaume-Uni", "Allemagne", "Thailande"]
    text_to_check = str(text).split()
    presence = 0
    found = ""
    for it, et in enumerate(text_to_check):
        for ic, ec in enumerate(list_contry):
            if et.lower() == ec.lower():
                found += ec
                presence += 1
    if presence == 1:
        status = True
    dict_response = {"status": status, "country": found}
    print("\ntext : {}\n".format(text))
    print("text_to_check : {}\n".format(text_to_check))
    print("status : {}\n".format(status))
    print("country : {}\n".format(country))
    print("presence : {}\n".format(presence))
    print("found : {}\n".format(found))
    print("dict_response : {}\n".format(dict_response))
    return dict_response





if __name__ == "__main__":
    #info = get_info_from_title("PARIS")
    #page_id = get_page_id_from_data(info)
    #article = get_article_wiki_by_pageid(page_id)
    #print(article)
    print("\nfirst try")
    is_country_known("paris chine allemagne")
    print("\nsecond try")
    is_country_known("allemagne ngiporengi opjegiezn ieoizgn")
