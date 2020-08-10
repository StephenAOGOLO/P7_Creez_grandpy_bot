from . import app
from flask import render_template, jsonify, request
from .utils import *
import logging as lg
lg.basicConfig(level=lg.INFO)


@app.route('/here')
@app.route('/index')
@app.route('/')
@app.route('/home')
def home():
    salutation = "bonjour"
    response = "Je vais vous répondre ..."
    place = {"lat": 16.25, "lng": -61.58333333, "search": False}
    return render_template("/interface/page.html", mot=salutation, response=response, place=place)


@app.route('/catcher', methods=["POST"])
def catcher():
    user_entry = request.form["research"]
    if is_entry_empty(user_entry)["status"]:
        return jsonify(is_entry_empty(user_entry)["text"])
    response = entry_treatment(user_entry)
    return jsonify(response)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/errors/404.html"), 404
