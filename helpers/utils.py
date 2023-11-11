import asyncio

import nest_asyncio


def as_cloud_function(fastapi_app, cloud_function_request):
    body = cloud_function_request.get_data(parse_form_data=False)
    scope = {
        "type": "http",
        "method": cloud_function_request.method,
        "headers": [(k.lower().encode(), v.encode()) for k, v in cloud_function_request.headers.items()],
        "path": cloud_function_request.path,
        "raw_path": cloud_function_request.path.encode(),
        "query_string": cloud_function_request.query_string,
        "scheme": "http",
        "server": None,
        "client": None,
        "root_path": "",
        "app": fastapi_app,
    }

    async def receive():
        return {
            "type": "http.request",
            "body": body,
            "more_body": False
        }

    response_body = []
    response_status = 200
    response_headers = []

    async def send(message):
        nonlocal response_body, response_status, response_headers
        if message["type"] == "http.response.start":
            response_status = message["status"]
            response_headers = message["headers"]
        elif message["type"] == "http.response.body":
            response_body.append(message.get("body", b""))

    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fastapi_app(scope, receive, send))

    return (b''.join(response_body), response_status, dict(response_headers))
