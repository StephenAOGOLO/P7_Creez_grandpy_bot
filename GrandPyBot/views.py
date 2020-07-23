from . import app
from flask import render_template, jsonify, request
from .utils import *
import logging as lg
lg.basicConfig(level=lg.INFO)


@app.route('/')
@app.route('/home')
def home():
    mot = "bonjour"
    response = "Je vais vous répondre ..."
    return render_template("/interface/page.html", mot=mot, response=response)


@app.route('/catcher', methods=["POST"])
def catcher():

    form_content = request.form["research"]
    lg.info("Before treatment>>>> : "+form_content)
    response = transform_to_upper(form_content)
    response = text_replace(response, "+")
    response = text_result(response)
    lg.info("after treatment>>>> : " + str(response))
    response = data_from_wiki(response)
    lg.info("after wiki treatment>>>> : " + str(response))
    response = str(response)
    print("type response: {}\n".format(type(response)))
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
