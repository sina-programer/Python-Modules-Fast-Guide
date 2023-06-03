import pickle


def dump(filepath, obj):
    with open(filepath, 'wb') as handler:
        return pickle.dump(obj, handler)


def load(filepath):
    with open(filepath, 'rb') as handler:
        return pickle.load(handler)
