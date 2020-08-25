""" Preparing operational functions with the "utils.py" module.
    - This module mainly works on text treatment.
    - It erases XSS breaches for avoid cross-scripting attacks.
    - It handles wrong user entries.
    - It parses the text to request APIs with the best data.
    - It formats the APIs response.
    - It provides prepared APIs responses to the "views.py" module."""
# -*- coding: utf-8 -*-
import requests as rqsts
import json
import random as rd
import logging as lg
lg.basicConfig(level=lg.INFO)


def gpb_messages(title, raw_text, file=".\\GrandPyBot\\static\\json\\gpb_messages.json"):
    messages = open_json_file(file)
    chance_h = rd.randrange(0, 10)
    chance_f = rd.randrange(0, 10)
    chance_h1 = rd.randrange(0, 6)
    chance_h2 = rd.randrange(0, 6)
    chance_h3 = rd.randrange(0, 6)
    header = messages["header"]
    footer = messages["footer"]
    header = header[chance_h]
    footer = footer[chance_f]
    h = messages["gpb"]
    h1 = title+messages["gpb_1"][chance_h1]
    h2 = messages["gpb_2"][chance_h2]
    h3 = messages["gpb_3"][chance_h3]
    h4 = messages["gpb_4"]
    haiku = h+h1+h2+h3+h4
    text = header+raw_text+haiku+footer
    return text


def get_coordinates(wiki_data, wiki_page_id, entry):
    status = False
    api = ""
    api_data = ""
    data_wiki = get_coordinates_from_wiki(wiki_data)
    data_osm = get_coordinates_from_osm(entry)
    if check_coordinates(data_wiki[str(wiki_page_id)]):
        api = "wiki"
        status = True
        api_data = data_wiki
    elif check_coordinates(data_osm):
        api = "osm"
        status = True
        api_data = data_osm
    report = {"status": status, "api": api, "data": api_data}
    return report


def check_coordinates(data):
    status = False
    if "coordinates" in data.keys():
        status = True
    return status


def get_coordinates_from_wiki(title):
    wikiUrl = "https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&&format=json&titles="
    url = wikiUrl+title
    data = rqsts.get(url)
    data = data.json()
    all_data = data["query"]["pages"]
    return all_data


def get_coordinates_from_osm(title):
    osm_url = "https://nominatim.openstreetmap.org/search.php?polygon_geojson=1&format=jsonv2&q="
    url = osm_url + title
    data = rqsts.get(url)
    data = data.json()
    data = data[0]
    all_data = {
        "all": data,
        "coordinates": data["geojson"],
        "lat": float(data["lat"]),
        "lon": float(data["lon"])}
    return all_data





def get_info_from_title(title):
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch='
    url = wikiUrl + str(title)
    all_data = rqsts.get(url)
    all_data = all_data.json()
    dict_data = {}
    try:
        all_data = all_data["query"]["search"]
        list_data = all_data
        for i, e in enumerate(list_data):
            dict_data[i] = e
        lg.debug("\n")
        lg.debug("Voici le contenu du dictionnaire :")
        lg.debug("\n")
        for k, v in dict_data.items():
            lg.debug("{} ----> {}".format(k, v))
    except Exception as e:
        lg.info("Erreur sur clé query : {}".format(e))
    return dict_data


def get_page_id_from_data(all_data):
    return all_data[0]["pageid"]


def get_article_wiki_by_pageid(page_id):
    """ paris = pageids=681159"""
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exsentences=2&explaintext=true&pageids='
    page_id = str(page_id)
    url = wikiUrl+page_id
    data_raw = rqsts.get(url)
    lg.debug(">> 1.1 - type: {}\n".format(type(data_raw)))
    lg.debug(">> 1.1 - valeur: {}\n".format(data_raw))
    dict_data = data_raw
    lg.debug(">> 2.1 - type: {}\n".format(type(dict_data)))
    lg.debug(">> 2.1 - valeur: {}\n".format(dict_data))
    data = dict_data.json()
    lg.debug(">> 3.1 - valeur: {}\n".format(data))
    article = data["query"]["pages"][page_id]["extract"]
    title = data["query"]["pages"][page_id]["title"]
    article = gpb_messages(title, article)
    #article = gpb_messages(title, article, ".\\static\\json\\gpb_messages.json")
    return article


def is_word_bad(first_list, second_list, delete=True):
    found = ""
    presence = 0
    status_presence = False
    raw_text = " ".join(first_list)
    for i1, e1 in enumerate(first_list):
        length_to_check = len(e1)
        if length_to_check < 10:
            for i2, e2 in enumerate(second_list[str(length_to_check)]):
                e2 = e2.replace("\n", "")
                if e1.lower() == e2.lower():
                    found += e1+" "
                    presence += 1
        else:
            for i2, e2 in enumerate(second_list["over_ten"]):
                e2 = e2.replace("\n", "")
                if e1.lower() == e2.lower():
                    found += e1+" "
                    presence += 1
    try:
        if delete:
            bad_words = found.split()
            count = {}.fromkeys(set(bad_words), 0)
            for w in bad_words:
                count[w] += 1
            for k, v in count.items():
                if v > 1:
                    for i in range(v-1):
                        bad_words.remove(k)
            for words in bad_words:
                occurences = first_list.count(words)
                for i in range(occurences):
                    first_list.remove(words)
    except Exception as e:
        lg.warning("erreur sur fonction 'is_bad_word()'\n>>{}".format(e))

    if presence > 0:
        status_presence = True
    treated_text = " ".join(first_list)
    dic_result = {"text_before": raw_text,
                  "text_after": treated_text,
                  "bad_words_presence": status_presence,
                  "bad_words": bad_words}
    lg.info("\n_| Rapport de traitement de saisie |_ \n{}\n".format(dic_result.items()))
    return dic_result


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

    if presence > 0:
        status_presence = True
    treated_text = " ".join(first_list)
    dic_result = {"text_before": raw_text,
                  "text_after": treated_text,
                  "bad_words_presence": status_presence,
                  "bad_words": bad_words}
    lg.info("\n_| Rapport de traitement de saisie |_ \n{}\n".format(dic_result.items()))
    return dic_result

def secure_text(text):
    #stop_words = stop_words_with_json(".\\static\\json\\bad_words.json")
    stop_words = stop_words_with_json()
    for c in stop_words["xss"]:
        if c in text:
            text = text.replace(c, "")
    lg.info("\nle texte saisie a été sécurisé avant son traitement\n")
    return text

def cleanup_text(text):
    text = secure_text(text)
    hashed_text = hash_text(text)
    #stop_words = stop_words_with_json(".\\static\\json\\bad_words.json")
    stop_words = stop_words_with_json()
    treatment_report = is_word_bad(hashed_text, stop_words)
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


def stop_words_with_json(file=".\\GrandPyBot\\static\\json\\bad_words.json"):
    stop_words = open_json_file(file)
    return stop_words


def is_entry_empty(text):
    status = False
    text = text.strip()
    if text == "":
        status = True
        text = "Pouvez-vous reformuler votre question ?"
    report = {"status": status, "text": text, "article": text}
    return report


def is_wrong_entry(data):
    status = True
    text = ""
    if len(data) == 0:
        status = False
        text = "Pouvez-vous reformuler votre question ?"
    report = {"status": status, "text": text}
    return report


def entry_treatment(text):
    output = {}
    lg.info("\nUser Entry >>>> : " + text)
    lg.info("\nMedia wiki API resqusting...\n")
    text = cleanup_text(text)
    if is_entry_empty(text)["status"]:
        output["article"] = is_entry_empty(text)["text"]
        return output
    output["info"] = get_info_from_title(text)
    report = is_wrong_entry(output["info"])
    if not report["status"]:
        output["article"] = report["text"]
        return output
    output["page_id"] = get_page_id_from_data(output["info"])
    output["article"] = str(get_article_wiki_by_pageid(output["page_id"]))
    lg.info("\nMedia wiki Response >>>> : " + output["article"]+"\n")
    lg.debug("type response: {}\n".format(type(output["article"])))
    info = output["info"]
    page_id = output["page_id"]
    wiki_data = info[0]["title"]
    result = get_coordinates(wiki_data, page_id, text)
    data = result["data"]
    location = {}
    if result["api"] == "wiki":
        location["lng"] = data[str(page_id)]["coordinates"][0]["lon"]
        location["lat"] = data[str(page_id)]["coordinates"][0]["lat"]
    elif result["api"] == "osm":
        location["lng"] = data["lon"]
        location["lat"] = data["lat"]
    location["zoom"] = 10
    location["search"] = True
    output["place"] = location
    lg.info("\nOUTPUT:\n{}\n".format(output))
    return output


if __name__ == "__main__":
    pass
