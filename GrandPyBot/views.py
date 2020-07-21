from . import app
from flask import render_template, jsonify, request


@app.route('/')
@app.route('/home')
def home():
    return render_template("/interface/page.html")


@app.route('/sender', methods=["POST"])
def sender():
    form_content = request.form["research"]
    print(">>>> : "+form_content)
    return jsonify(['Pas de reponse'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/errors/404.html"), 404
