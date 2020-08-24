from . import app
from flask import render_template, jsonify, request
from .utils import *
import logging as lg
from . import config
lg.basicConfig(level=lg.INFO)


@app.route('/')
@app.route('/home')
def home():
    gmap_id = str(config.GMAP_ID)
    gmap_url = "https://maps.googleapis.com/maps/api/js?callback=initMap&key="
    gmap_url = gmap_url + gmap_id
    salutation = "Bien le bonjour !! Je suis GrandPyBot!! Posez-moi une question et je vais tenter de vous répondre."
    designer = "Stephen A.OGOLO - https://github.com/StephenAOGOLO/P7_Creez_grandpy_bot.git"
    place = {"lat": 16.25, "lng": -61.58333333, "search": False}
    return render_template("/interface/page.html", mot=salutation, designer=designer, place=place, gmap_url=gmap_url)


@app.route('/catcher', methods=["POST"])
def catcher():
    response = {}
    user_entry = request.form["research"]
    if is_entry_empty(user_entry)["status"]:
        response["article"] = is_entry_empty(user_entry)["text"]
    else:
        response = entry_treatment(user_entry)
        response["gmap_id"] = str(config.GMAP_ID)
        print("fin")
    return jsonify(response)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/errors/404.html"), 404
