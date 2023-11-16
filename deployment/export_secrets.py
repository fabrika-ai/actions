def generate_env_vars_string():
    from actions.api_keys import API_KEYS  # Adjust the import path as necessary
    env_vars = [f"{key}" + "=${{secrets." + f"{key}" + "}}" for key in API_KEYS]
    return ",".join(env_vars)


if __name__ == "__main__":
    print(generate_env_vars_string())
