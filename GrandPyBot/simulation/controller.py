#from flask import Flask
#from . import views
#from flask_sqlalchemy import SQLAlchemy
#from GrandPyBot.simulation.mocks import Sentence

#controller = Flask(__name__)
#controller.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/p7.db"
#controller.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db = SQLAlchemy(controller)
#
#
#class Question(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    quest = db.Column(db.String(255))
#    resp = db.Column(db.String(255))
#
#    def __repr__(self):
#        return '<Question %r>' % self.quest
#
#
#db.create_all()


#if __name__ == "__main__":
#    """ Main """
#    controller.run()
