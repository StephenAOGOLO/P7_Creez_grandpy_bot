# -*- coding: utf-8 -*-
import requests as rqsts
import json
import time
import logging as lg
lg.basicConfig(level=lg.INFO)

def get_coordinates_from_title(title):
    wikiUrl = "https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&&format=json&titles="
    url = wikiUrl+title
    all_data = rqsts.get(url)
    all_data = all_data.json()
    all_data = all_data["query"]["pages"]
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
    return data["query"]["pages"][page_id]["extract"]


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


def cleanup_text(text):
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
    report = {"status": status, "text": text}
    return report


def entry_treatment(text):
    output = {}
    lg.info("\nUser Entry >>>> : " + text)
    lg.info("\nMedia wiki API resqusting...\n")
    text = cleanup_text(text)
    if is_entry_empty(text)["status"]:
        return is_entry_empty(text)["text"]
    output["info"] = get_info_from_title(text)
    output["page_id"] = get_page_id_from_data(output["info"])
    output["article"] = str(get_article_wiki_by_pageid(output["page_id"]))
    lg.info("\nMedia wiki Response >>>> : " + output["article"]+"\n")
    lg.debug("type response: {}\n".format(type(output["article"])))
    info = output["info"]
    page_id = output["page_id"]
    data = get_coordinates_from_title(info[0]["title"])
    location = {}
    location["lng"] = data[str(page_id)]["coordinates"][0]["lon"]
    location["lat"] = data[str(page_id)]["coordinates"][0]["lat"]
    location["search"] = True
    output["place"] = location
    lg.info("\nOUTPUT:\n{}\n".format(output))
    return output


if __name__ == "__main__":
    #pass
    entry_treatment("ou se trouve openclassrooms")







