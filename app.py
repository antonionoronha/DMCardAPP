from flask import Flask, Blueprint
from DMCard.restplus import api
from DMCard.endpoints.solicitation import ns_solicitation
from DMCard.db import config_db
from DMCard.log import log
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False
    app.config['CORS_HEADERS'] = 'Content-Type'

    config_db(app)
    blueprint = Blueprint('api', __name__)
    CORS(blueprint)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(ns_solicitation)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(port=5000)


if __name__ == '__main__':
    main()