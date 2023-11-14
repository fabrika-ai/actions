import json
import requests
import urllib.parse

BASE_URL = 'https://actions.tryfabrika.com/'
BASE_OPENAPI_CONFIG = {
    "openapi": "3.1.0",
    "info": {
        "title": "Fabrika",
        "version": "alpha"
    },
    "servers": [
        {
            "url": BASE_URL
        }
    ],
    "paths": {},
    "components": {},
}


def merge_openapi_schemas(function_names):
    merged_schema = BASE_OPENAPI_CONFIG.copy()

    for function_name in function_names:
        schema = get_schema_from_url(
            urllib.parse.urljoin(BASE_URL, function_name + "/openapi.json")
        )
        merged_schema["paths"].update(get_paths(schema, function_name))
        merged_schema["components"].update(schema.get("components", {}))

    return merged_schema


def get_schema_from_url(url):
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching schema from {url}: {e}")
        return None


def get_paths(schema, url):
    paths = {}
    for key, value in schema.get('paths', {}).items():
        paths[f"/{url}{key}"] = value
    return paths


functions = ['template', 'yfinance']

merged_schema = merge_openapi_schemas(functions)
if merged_schema:
    print(json.dumps(merged_schema, indent=4))
else:
    print("Failed to merge schemas.")
