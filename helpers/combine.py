import json
import requests
import urllib.parse

BASE_URL = 'https://us-central1-fabrika-404805.cloudfunctions.net/'


def merge_openapi_schemas(function_names):
    merged_schema = None

    for function_name in function_names:
        schema = get_schema_from_url(
            urllib.parse.urljoin(BASE_URL, function_name + "/openapi.json")
        )

        if schema is None:
            return None

        if merged_schema is None:
            merged_schema = schema
            # Prefix the initial paths with the function name
            merged_schema['paths'] = {f"/{function_name}{key}": value for key, value in schema['paths'].items()}
        else:
            # Update paths with new function name prefix
            new_paths = {f"/{function_name}{key}": value for key, value in schema['paths'].items()}
            merged_schema['paths'].update(new_paths)

            # Merge components
            merged_schema['components'].update(schema.get('components', {}))

            # Merge servers - ensuring no duplicates
            servers = set(json.dumps(server) for server in merged_schema.get('servers', []))
            servers.update(json.dumps(server) for server in schema.get('servers', []))
            merged_schema['servers'] = [json.loads(server) for server in servers]

    return merged_schema


def get_schema_from_url(url):
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


functions = ['sum-of-2-values', 'stock-price-data']

merged_schema = merge_openapi_schemas(functions)
if merged_schema:
    print(json.dumps(merged_schema, indent=4))
else:
    print("Failed to merge schemas.")
