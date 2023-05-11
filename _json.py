import json


def dump_json(obj, filepath):  # or json.dumps(string)
    with open(filepath, 'w') as handler:
        return json.dump(obj, handler, indent=4)


def load_json(filepath):  # or json.loads(string)
    with open(filepath) as handler:
        return json.load(handler)
