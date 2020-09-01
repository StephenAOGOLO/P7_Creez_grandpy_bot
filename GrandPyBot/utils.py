""" Preparing operational functions with the "utils.py" module.
    - This module mainly works on text treatment.
    - It erases XSS breaches for avoid cross-scripting attacks.
    - It handles wrong user entries.
    - It parses the text to request APIs with the best data.
    - It formats the APIs response.
    - It provides prepared APIs responses to the "views.py" module."""
# -*- coding: utf-8 -*-
import logging as lg
import json
import random as rd
import requests as rqsts
import GrandPyBot.options as opt
import os
lg.basicConfig(level=lg.INFO)


class Loading:
    """
    This class manage data parameters stored in a external file.
    """
    def __init__(self):
        """
        This constructor create a instance
        which contains all the data from a file ini.
        """
        the_options = opt.Settings()
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.msg = the_options.get_data_file_ini("msg")
        self.api = the_options.get_data_file_ini("api")
        self.parse = the_options.get_data_file_ini("parse")
        self.stop_words = self.parse["stop_words"]

    def gpb_messages(self, title, raw_text):
        """ This method provides personal messages into the GPB response """
        gpb_msg = self.msg["gpb_msg"]
        gpb_msg = self.basedir + gpb_msg
        messages = open_json_file(gpb_msg)
        h_1 = rd.randrange(0, 10)
        f_1 = rd.randrange(0, 10)
        h10 = rd.randrange(0, 6)
        h20 = rd.randrange(0, 6)
        h30 = rd.randrange(0, 6)
        header = messages["header"]
        footer = messages["footer"]
        header = header[h_1]
        footer = footer[f_1]
        h_1 = messages["gpb"]
        h10 = title+messages["gpb_1"][h10]
        h20 = messages["gpb_2"][h20]
        h30 = messages["gpb_3"][h30]
        h40 = messages["gpb_4"]
        haiku = h_1+h10+h20+h30+h40
        text = header+raw_text+haiku+footer
        msg = {"text": text, "haiku": haiku}
        return msg

    def get_coordinates_from_wiki(self, title):
        """ This method obtain longitude and latitude
        from a WikiPedia title """
        wiki_coordinates = self.api["wiki_coordinates"]
        url = wiki_coordinates+title
        data = rqsts.get(url)
        data = data.json()
        all_data = data["query"]["pages"]
        return all_data

    def get_coordinates_from_osm(self, title):
        """ This method obtain longitude and latitude
        from OpenStreetMap Api """
        osm_coordinates = self.api["osm_coordinates"]
        url = osm_coordinates + title
        data = rqsts.get(url)
        data = data.json()
        data = data[0]
        all_data = {
            "all": data,
            "coordinates": data["geojson"],
            "lat": float(data["lat"]),
            "lon": float(data["lon"])}
        return all_data

    def get_info_from_title(self, title):
        """ This method obtain all raw informations from WikiPedia title """
        wiki_info_from_title = self.api["wiki_info_from_title"]
        url = wiki_info_from_title + str(title)
        all_data = rqsts.get(url)
        all_data = all_data.json()
        dict_data = {}
        try:
            all_data = all_data["query"]["search"]
            list_data = all_data
            for i_1, e_1 in enumerate(list_data):
                dict_data[i_1] = e_1
        except Exception as e_1:
            lg.info("Erreur sur clé query : %s", e_1)
        return dict_data

    def get_article_wiki_by_pageid(self, page_id):
        """ This method obtain the relative article
        with a WikiPedia page id """
        wiki_art_by_pageid = self.api["wiki_art_by_pageid"]
        page_id = str(page_id)
        url = wiki_art_by_pageid + page_id
        data_raw = rqsts.get(url)
        dict_data = data_raw
        data = dict_data.json()
        article = data["query"]["pages"][page_id]["extract"]
        title = data["query"]["pages"][page_id]["title"]
        article = self.gpb_messages(title, article)["text"]
        haiku = self.gpb_messages(title, article)["haiku"]
        article = {"article": article, "haiku": haiku}
        return article

    def stop_words_with_json(self):
        """ This method provides all the forbidden characters """
        self.stop_words = self.basedir + self.stop_words
        stop_words = open_json_file(self.stop_words)
        return stop_words


def get_coordinates(wiki_data, wiki_page_id, entry):
    """ This function report coordinates status
    from WikiPedia and OpenStreetMap Apis """
    load = Loading()
    status = False
    api = ""
    api_data = ""
    data_wiki = load.get_coordinates_from_wiki(wiki_data)
    data_osm = load.get_coordinates_from_osm(entry)
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
    """ This function verifies if coordinates have been found """
    status = False
    if "coordinates" in data.keys():
        status = True
    return status


def get_page_id_from_data(all_data):
    """ This function obtain the page id from a WikiPedia raw data """
    return all_data[0]["pageid"]


def is_word_bad(first_list, second_list, delete=True):
    """ This function parses a text to provided only essential data """
    found = ""
    presence = 0
    status_presence = False
    raw_text = " ".join(first_list)
    for e_1 in first_list:
        length_to_check = len(e_1)
        if length_to_check < 11:
            for e_2 in second_list[str(length_to_check)]:
                e_2 = e_2.replace("\n", "")
                if e_1.lower() == e_2.lower():
                    found += e_1+" "
                    presence += 1
        else:
            for e_2 in second_list["over_ten"]:
                e_2 = e_2.replace("\n", "")
                if e_1.lower() == e_2.lower():
                    found += e_1+" "
                    presence += 1
    try:
        if delete:
            bad_words = found.split()
            count = {}.fromkeys(set(bad_words), 0)
            for w_1 in bad_words:
                count[w_1] += 1
            for k_1, v_1 in count.items():
                if v_1 > 1:
                    for i_1 in range(v_1 - 1):
                        bad_words.remove(k_1)
            for words in bad_words:
                occurences = first_list.count(words)
                for i_1 in range(occurences):
                    first_list.remove(words)
    except Exception as e_1:
        lg.warning("erreur sur fonction 'is_bad_word()'\n>>%s", e_1)
    if presence > 0:
        status_presence = True
    treated_text = " ".join(first_list)
    dict_result = {"text_before": raw_text,
                  "text_after": treated_text,
                  "bad_words_presence": status_presence,
                  "bad_words": bad_words}
    return dict_result


def secure_text(text):
    """ This function handles XSS breaches """
    load = Loading()
    stop_words = load.stop_words_with_json()
    for c_1 in stop_words["xss"]:
        if c_1 in text:
            text = text.replace(c_1, "")
    return text


def cleanup_text(text):
    """ This function handles the parsing functions """
    load = Loading()
    text = secure_text(text)
    hashed_text = hash_text(text)
    stop_words = load.stop_words_with_json()
    treatment_report = is_word_bad(hashed_text, stop_words)
    cleaned_word = treatment_report["text_after"]
    return cleaned_word


def hash_text(text):
    """ This function transfoms text entry into a treatable text """
    return str(text).split()


def open_json_file(json_file):
    """'open_json_file' function read a given json file.
    It returns the content file into a dict."""
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)
    return data


def is_entry_empty(text):
    """ This function checks if no words is given for search """
    status = False
    text = text.strip()
    if text == "":
        status = True
        text = "Pouvez-vous reformuler votre question ?"
    report = {"status": status, "text": text, "article": text}
    return report


def is_wrong_entry(data):
    """ This function checks if only bad words is given for search """
    status = True
    text = ""
    if len(data) == 0:
        status = False
        text = "Pouvez-vous reformuler votre question ?"
    report = {"status": status, "text": text}
    return report


def choose_geocoding(data, result, page_id):
    """ This function reports which geocoding Api is used """
    location = {}
    if result["api"] == "wiki":
        location["lng"] = data[str(page_id)]["coordinates"][0]["lon"]
        location["lat"] = data[str(page_id)]["coordinates"][0]["lat"]
    elif result["api"] == "osm":
        location["lng"] = data["lon"]
        location["lat"] = data["lat"]
    return location


def entry_treatment(text):
    """ This function handles the whole process
     from the received text entry to the Apis response """
    output = {}
    load = Loading()
    text = cleanup_text(text)
    if is_entry_empty(text)["status"]:
        output["article"] = is_entry_empty(text)["text"]
        return output
    output["info"] = load.get_info_from_title(text)
    report = is_wrong_entry(output["info"])
    if not report["status"]:
        output["article"] = report["text"]
        return output
    output["page_id"] = get_page_id_from_data(output["info"])
    output["article"] = str(load.get_article_wiki_by_pageid(output["page_id"])["article"])
    output["haiku"] = str(load.get_article_wiki_by_pageid(output["page_id"])["haiku"])
    info = output["info"]
    page_id = output["page_id"]
    wiki_data = info[0]["title"]
    result = get_coordinates(wiki_data, page_id, text)
    output["report"] = result
    data = result["data"]
    location = choose_geocoding(data, result, page_id)
    location["zoom"] = 10
    location["search"] = True
    output["place"] = location
    lg.info("\nOUTPUT:\n%s\n", output)
    return output
