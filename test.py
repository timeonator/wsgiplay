from io import BytesIO

def get(app, path = '/', query = ''):
    response_status = []
    response_headers = []

    def start_response(status, headers):
        status = status.split(' ', 1)
        response_status.append((int(status[0]), status[1]))
        response_headers.append(dict(headers))

    environ = {
        'HTTP_ACCEPT': '*/*',
        'HTTP_HOST': '127.0.0.1:8000',
        'HTTP_USER_AGENT': 'TestAgent/1.0',
        'PATH_INFO': path,
        'QUERY_STRING': query,
        'REQUEST_METHOD': 'GET',
        'SERVER_NAME': '127.0.0.1',
        'SERVER_PORT': '8000',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'SERVER_SOFTWARE': 'TestServer/1.0',
        'wsgi.errors': BytesIO(b''),
        'wsgi.input': BytesIO(b''),
        'wsgi.multiprocess': False,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'http',
        'wsgi.version': (1, 0),
    }

    response_body = app(environ, start_response)
    merged_body = ''.join((x.decode('utf-8') for x in response_body))

    if hasattr(response_body, 'close'):
        response_body.close()

    return {'status': response_status[0],
            'headers': response_headers[0],
            'body': merged_body}

