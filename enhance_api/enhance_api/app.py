### Import the libraries required
from flask import Flask
from flask import request, jsonify
from get_img import get_image
import pandas as pd
from flask_httpauth import HTTPBasicAuth
from werkzeug.exceptions import BadRequest, Forbidden, HTTPException, NotFound
import pickle
import threading
import asyncio
import time
from flask_cors import CORS

from flask import abort
import logging
logger = logging.getLogger()
logger.disabled = True
## Initiating the serve
server = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
CORS(server)

# basic authentication
auth = HTTPBasicAuth()

# creds
users = {
    "john": "hello",
    "admin": "pwd",
}


@auth.get_password
def get_pw(username):
    if username in users:
        server.logger.info('user_name_authenticated')
        return users.get(username)
    return None


@server.route('/clean_img', methods=['POST'])
# @auth.login_required
def predicttwo():
    '''
    :return: decile score and id wrt tier three.
    '''
    try:
        data = request.get_json(force=True)
        data = data['data']
        # server.logger.info("requested_the Payload{0}".format(data))

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        result = loop.run_until_complete(get_image(data))
        print("SUCESSFUL")
        # result = get_image(data)
        # server.logger.info("score and decile respectively {0} \n".format(result))
        return result
        
    except KeyError as e:
            server.logger.error("Input request error{0}".format(e))
            return jsonify({"MESSAGE": str(e) + "Recheck the payload"})
    except BadRequest as e:
        server.logger.error("Input request error{0}".format(e))
        return {"message": str(e)}
    except TypeError as e:
        server.logger.error("Input request error{0}".format(e))
        return {"message": str(e)}
