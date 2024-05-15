from json import load

with open("../env.json") as env_file:
    ENV = load(env_file)