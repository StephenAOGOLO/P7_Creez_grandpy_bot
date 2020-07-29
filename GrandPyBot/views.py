from . import app
from flask import render_template, jsonify, request
from .utils import *
import logging as lg
lg.basicConfig(level=lg.INFO)


@app.route('/')
@app.route('/home')
def home():
    salutation = "bonjour"
    response = "Je vais vous répondre ..."
    return render_template("/interface/page.html", mot=salutation, response=response)


@app.route('/catcher', methods=["POST"])
def catcher():

    user_entry = request.form["research"]
    response = entry_treatment(user_entry)
    #lg.info("\nUser Entry >>>> : "+user_entry)
    ##user_entry = text_replace(user_entry, "+")
    #lg.info("Media wiki API resqusting...")

    #user_entry = is_country_known(user_entry)
    #user_entry = user_entry["country"]

    #response = get_info_from_title(user_entry)
    #response = get_page_id_from_data(response)
    #response = get_article_wiki_by_pageid(response)
    #lg.info("Media wiki Response >>>> : " + str(response))
    #response = str(response)
    #print("type response: {}\n".format(type(response)))
    return jsonify(response)


@app.route('/sender_01')
def sender_01():
    response = start_wiki()
    return render_template("/interface/page.html", response=response)


@app.route('/sender')
def sender():
    return render_template("/errors/in_progress.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/errors/404.html"), 404
