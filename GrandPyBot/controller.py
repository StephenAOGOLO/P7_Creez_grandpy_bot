from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from GrandPyBot.simulation.mocks import Sentence

controller = Flask(__name__)
controller.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/p7.db"
controller.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(controller)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest = db.Column(db.String(255))
    resp = db.Column(db.String(255))

    def __repr__(self):
        return '<Question %r>' % self.quest


db.create_all()


@controller.route('/')
def hello_world():
    return 'Bonjour !!'


@controller.route('/home')
def home():
    return render_template("/interface/home.html")


@controller.errorhandler(404)
def page_not_found(error):
    return render_template("/errors/404.html"), 404


if __name__ == "__main__":
    """ Main """
    controller.run()
