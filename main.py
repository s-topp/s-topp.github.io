from flask import Flask
from flask_restful import Resource, Api, reqparse
#from base64 import decodebytes
import base64
import math
import codecs


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


parser = reqparse.RequestParser()
parser.add_argument('data')


class StyleId(Resource):
    def post(self):
        args = parser.parse_args()
        data = args['data']
        # l = len(data)
        # padded_data = data.ljust(int(math.ceil(l / 4.0) * 4), '=')
        data = bytes(data)
        strOne = data.partition(",")[2]
        pad = len(strOne) % 4
        strOne += b"=" * pad
        with open("image.png", "wb") as fh:
            fh.write(strOne.decode('base64'))
        return "done :D"

api.add_resource(HelloWorld, '/')
api.add_resource(StyleId, '/get_style_id')

if __name__ == '__main__':
    app.run(debug=True)
