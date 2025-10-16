from optparse import Values
def get_keys(data):
    """
    Returns a list of all keys in the dictionary.
    """
    return data.keys() if data else []

def get_values(data):
    """
    Returns a list of all values in the dictionary.
    """
    return data.values() if data else []

def get_items(data):
    """
    Returns a list of all key-value pairs (tuples) in the dictionary.
    """
    return data.items() if data else []

def get_value(data, key, default=None):
    """
    Returns the value for the given key if it exists, otherwise returns the default value.
    """
    return data.get(key, default) if data else []
