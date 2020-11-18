from server import app
from flask import request, send_file, jsonify

from src.getFramesFromGIF import getFramesFromGIFObject
from src.getMCFunction import getMCFunction

import base64 as b64
from io import BytesIO

@app.route('/api/generate', methods = ['POST'])
def generate_gif():

    # just some really dumb error handling for now
    try:
        # forming that data into something useful
        data = request.get_json()
        image_data = b64.urlsafe_b64decode(data['img'])

        # getting a file object from the data for the rest of the program to
        # to work with
        file_ob = BytesIO()
        file_ob.write(image_data)
        file_ob.seek(0)

        # sending the file to the converter
        frames = getFramesFromGIFObject(file_ob)

    # if something goes wrong...
    except Exception as e:
        response = jsonify({"status": "failed"})
        response.status_code = 400
        return response
