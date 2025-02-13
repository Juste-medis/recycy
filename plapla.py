
def create_app():
    method = environ['REQUEST_METHOD']
    path_info = environ.get('PATH_INFO', '/')

    if method == 'POST' and path_info == '/data':
        try:
            # Lire la longueur des données entrantes
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            post_data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
            
            # Traiter les données reçues
            data = json.loads(post_data.decode())
            1/0
            response_body = json.dumps({"message": "Data received successfully", "data": data})
    
            status = '200 OK'
            headers = [('Content-Type', 'application/json')]
        except Exception as e:
            response_body = json.dumps({"error": str(e)})
            status = '400 Bad Request'
            headers = [('Content-Type', 'application/json')]
        
    else:
        response_body = 'It works!\nPython %s\n' % sys.version.split()[0]
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    return [response_body.encode()]














import sys
import os
import json
from werkzeug.wrappers import Response
from werkzeug.exceptions import HTTPException

os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

def application(environ, start_response):
    """WSGI wrapper for the Flask app."""
    # app = create_app()

    method = environ['REQUEST_METHOD']
    path_info = environ.get('PATH_INFO', '/')

    if method == 'POST' and path_info == '/data':
        try:
            # Lire la longueur des données entrantes
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            post_data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
            
            # Traiter les données reçues
            data = json.loads(post_data.decode())
            1/0
            response_body = json.dumps({"message": "Data received successfully", "data": data})
    
            status = '200 OK'
            headers = [('Content-Type', 'application/json')]
        except Exception as e:
            response_body = json.dumps({"error": str(e)})
            status = '400 Bad Request'
            headers = [('Content-Type', 'application/json')]
        
    else:
        response_body = 'It works!\nPython %s\n' % sys.version.split()[0]
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    return [response_body.encode()]

    # with app.request_context(environ):
    #     try:
    #         response = app.full_dispatch_request()
    #     except HTTPException as e:
    #         response = e.get_response()
        
    #     status = f"{response.status_code} {response.status}"
    #     headers = [(key, value) for key, value in response.headers]

    #     start_response(status, headers)
    #     return [response.get_data()]

