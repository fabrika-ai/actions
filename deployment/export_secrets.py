# export_secrets.py

def generate_export_commands():
    from actions.api_keys import API_KEYS  # Adjust the import path as necessary
    commands = []
    for key in API_KEYS:
        commands.append(f"echo 'export {key}=${{{key}}}'")
    return commands

if __name__ == "__main__":
    for cmd in generate_export_commands():
        print(cmd)
