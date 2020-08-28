""" Preparing routes with the "views.py" module.
    - This module has a gateway purpose between
     the operational functions "utils.py" and the HMI
    - It mainly catching and sending data
     from and towards the application front-side. """
# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request
from . import app
from .utils import is_entry_empty, entry_treatment
from . import config


@app.route('/')
@app.route('/home')
def home():
    """ This function creates a route
        allowing the client user to reach the one-page site.
        It mainly returns messages to display on."""
    gmap_id = str(config.GMAP_ID)
    gmap_url = "https://maps.googleapis.com/maps/api/js?callback=initMap&key="
    gmap_url = gmap_url + gmap_id
    salutation = " Je suis GrandPyBot!! Tu veux connaitre un lieu ?" \
                 " Pose-moi ta question et je vais tenter de te répondre."
    designer = "Stephen A.OGOLO" \
               " - https://github.com/StephenAOGOLO/P7_Creez_grandpy_bot.git"
    place = {"lat": 16.25, "lng": -61.58333333, "search": False}
    return render_template("/interface/page.html",
                           mot=salutation,
                           designer=designer,
                           place=place,
                           gmap_url=gmap_url)


@app.route('/catcher', methods=["POST"])
def catcher():
    """
    This function is the route which is the core
    of the gateway between the operational functions and HMI.
    It catches all data seized by the client user
    and send it to the op-functions.

    Once treatment is over,
    it retrieve prepared data and provide it to the HMI.
    """
    response = {}
    user_entry = request.form["research"]
    if is_entry_empty(user_entry)["status"]:
        response["article"] = is_entry_empty(user_entry)["text"]
    else:
        response = entry_treatment(user_entry)
        print("fin")
    return jsonify(response)


@app.errorhandler(404)
def page_not_found(error):
    """ This function handling wrong urls.
        It returns 404 error on the one-page website"""
    return render_template("/errors/404.html"), 404
