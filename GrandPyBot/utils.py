import requests as rqsts


def transform_to_upper(text):
    return {"text-original": text, "text-transformed": text.upper()}


def text_parser(text, sep=" "):
    data = text["text-transformed"]
    data = data.split(sep)
    text["text-transformed"] = data
    return text


def text_replace(text, sep="+"):
    data = text["text-transformed"]
    data = data.replace(' ', sep)
    text["text-transformed"] = data
    return text


def text_result(text):
    return text["text-transformed"]


def data_from_wiki(text):
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=opensearch&format=json&search='
    url = wikiUrl+text
    data_raw = rqsts.get(url)
    print(">> 1 - type: {}\n".format(type(data_raw)))
    print(">> 1 - valeur: {}\n".format(data_raw))
    data_json = data_raw.json()
    print(">> 2 - type: {}\n".format(type(data_json)))
    print(">> 2 - valeur: {}\n".format(data_json))
    browse_data(data_json)
    print(">> 4 - type: {}\n".format(type(data_json[1][1])))
    return data_json[1][1]


def browse_data(data):
    print("Le type de cette donnée est: {}\n".format(type(data)))
    #for e in data:
    #    print(e)
    print("\n")
    print(">> 3 - type: {}\n".format(type(data[1][1])))
    print(data[1][1])
    print("\n")


def start_wiki():
    wikiUrl = 'https://fr.wikipedia.org/w/api.php?action=opensearch&format=json&search=francais'
    data_raw = rqsts.get(wikiUrl)
    data_json = data_raw.json()
    return data_json[1][1]
