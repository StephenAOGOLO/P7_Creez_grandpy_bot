from flask import Flask, render_template

controller = Flask(__name__)


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
