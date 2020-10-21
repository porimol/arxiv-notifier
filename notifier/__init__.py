# coding=utf-8
from flask import Flask
from flask import render_template
from flask import jsonify
from flask_compress import Compress
from flask_cors import CORS


server = Flask(__name__)
# Configurations
server.config.from_object('config')

@server.errorhandler(404)
def not_found(error):
    print("Error Message: {0}".format(error))
    # return render_template('404.html', response=error), 404
    error_response = {
        "message": "Error Message: {0}".format(error)
    }
    return jsonify(error_response)

# Import a module / component using its blueprint handler variable (mod_auth)
from notifier.app import notify_routers

# Register blueprint(s)
server.register_blueprint(notify_routers)
CORS(server)
Compress(server)

# print all of the routes path
endpoints = [rule.rule for rule in server.url_map.iter_rules()]
print(endpoints)
