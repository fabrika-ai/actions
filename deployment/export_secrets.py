import os
import json


def export_secrets():
    api_keys_file = 'actions/api_keys.py'
    namespace = {}
    with open(api_keys_file) as f:
        exec(f.read(), namespace)

    api_keys = namespace['API_KEYS']
    secrets = json.loads(os.environ['SECRETS'])

    for key in api_keys:
        os.environ[key] = secrets.get(key, '')


if __name__ == "__main__":
    export_secrets()
