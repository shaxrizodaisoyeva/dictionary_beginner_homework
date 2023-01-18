def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    a=[]
    for b in data.keys():
        if type(b)==int:
            a.append(b)
    return a
data={1: 'a', 'job':'developer', 'name': 'b', '2':'teacher', 'name':'c', 4:'teacher'}
print(find_int_keys(data))
