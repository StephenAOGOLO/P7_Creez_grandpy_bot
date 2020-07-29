# -*- coding: utf-8 -*-
import requests as rqsts
import json
import time
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

def is_word_in(first_list, second_list, delete=True):
    found = ""
    presence = 0
    status_presence = False
    raw_text = " ".join(first_list)
    for i1, e1 in enumerate(first_list):
        for i2, e2 in enumerate(second_list):
            e2 = e2.replace("\n", "")
            if e1.lower() == e2.lower():
                found += e1+" "
                presence += 1
    if delete:
        bad_words = found.split()
        for words in bad_words:
            first_list.remove(words)
            #first_list.remove(e1)

    if presence > 0:
        status_presence = True
    treated_text = " ".join(first_list)
    dic_result = {"text_before": raw_text,
                  "text_after": treated_text,
                  "bad_words_presence": status_presence,
                  "bad_words": bad_words}
    lg.info("_| Rapport de traitement de saisie |_ \n{}".format(dic_result.items()))
    return dic_result


def cleanup_text(text):
    hashed_text = hash_text(text)
    #stop_words = stop_words_with(".\\static\\txt\\test.txt")
    stop_words = stop_words_with(".\\GrandPyBot\\static\\txt\\test.txt")
    treatment_report = is_word_in(hashed_text, stop_words)
    cleaned_word = treatment_report["text_after"]
    return cleaned_word


def hash_text(text):
    return str(text).split()


def open_json_file(json_file):
    """'open_json_file' method read a given json file.
    It returns the content file into a dict."""
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)
    return data

def create_file(path_fichier="./",name_fichier="fichier_genere_par_python" ,extension="txt", contenu = "vide"):

    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    creation_time = "_"+when_happens
    print("=" * 150)
    new_file = open(path_fichier+"//"+name_fichier+creation_time+"."+extension, "wt")
    for ligne in contenu:
        new_file.write(ligne)
    new_file.close
    print("le fichier '{}.{}' est prêt".format(name_fichier,extension))


def open_file(path_fichier):
    """ Fonction d'ouverture d'un fichier
                        et
        sauvegrade du contenu en mémoire

    :param path_fichier:
    :return liste_fichier: """

    with open(path_fichier,"rt") as fichier:
        liste_fichier = fichier.readlines()
    lg.debug("=" * 150)
    lg.debug("\nVoici le contenu du fichier : {}\n".format(path_fichier))
    for indice, ligne in enumerate(liste_fichier):
        lg.debug("ligne {} : {}".format(indice, ligne))
    lg.debug("=" * 150)
    lg.debug("\nFin de fichier\n")
    lg.debug("=" * 150)
    return liste_fichier

def stop_words_with(file=".\\GrandPyBot\\static\\txt\\all_stop_words.txt"):
    stop_words = open_file(file)
    return stop_words


def entry_treatment(text):
    lg.info("\nUser Entry >>>> : " + text)
    lg.info("Media wiki API resqusting...")
    text = cleanup_text(text)
    #text = is_country_known(text)
    #text = text["country"]
    text = get_info_from_title(text)
    text = get_page_id_from_data(text)
    text = get_article_wiki_by_pageid(text)
    lg.info("Media wiki Response >>>> : " + str(text))
    text = str(text)
    print("type response: {}\n".format(type(text)))
    return text

if __name__ == "__main__":
    #pass
    #info = get_info_from_title("PARIS")
    #page_id = get_page_id_from_data(info)
    #article = get_article_wiki_by_pageid(page_id)
    #print(article)

    #print("\nfirst try")
    #is_country_known("paris chine allemagne")
    #print("\nsecond try")
    #is_country_known("allemagne ngiporengi opjegiezn ieoizgn")

    #text = entry_treatment("brésil")
    #print(text)

    all_words = open_file(".\\static\\txt\\all_stop_words.txt")
    print(type(all_words))

    dict_all_words = {}
    liste_1 = []
    liste_2 = []
    liste_3 = []
    liste_4 = []
    liste_5 = []
    liste_6 = []
    liste_7 = []
    liste_8 = []
    liste_9 = []
    liste_10 = []
    liste_x = []
    for word in all_words:
        word = word.replace("\n", "")
        index = 1
        if len(word) == index:
            liste_1.append(word)
            dict_all_words[str(index)] = liste_1
            #break
        index += 1
        if len(word) == index:
            liste_2.append(word)
            dict_all_words[str(index)] = liste_2
            #break
        index += 1
        if len(word) == index:
            liste_3.append(word)
            dict_all_words[str(index)] = liste_3
            #break
        index += 1
        if len(word) == index:
            liste_4.append(word)
            dict_all_words[str(index)] = liste_4
            #break
        index += 1
        if len(word) == index:
            liste_5.append(word)
            dict_all_words[str(index)] = liste_5
            #break
        index += 1
        if len(word) == index:
            liste_6.append(word)
            dict_all_words[str(index)] = liste_6
            #break
        index += 1
        if len(word) == index:
            liste_7.append(word)
            dict_all_words[str(index)] = liste_7
            #break
        index += 1
        if len(word) == index:
            liste_8.append(word)
            dict_all_words[str(index)] = liste_8
            #break
        index += 1
        if len(word) == index:
            liste_9.append(word)
            dict_all_words[str(index)] = liste_9
            #break
        index += 1
        if len(word) == index:
            liste_10.append(word)
            dict_all_words[str(index)] = liste_10
            #break
        index += 1
        if len(word) > index:
            liste_x.append(word)
            dict_all_words["over_ten"] = liste_x
            #break
    print("fin")



