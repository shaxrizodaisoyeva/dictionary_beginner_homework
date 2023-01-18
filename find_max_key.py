def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    a=0 
    b=[]
    while a<len(data):
        b+=data.keys()
        a +=1
    c=max(b)
    return c
data={3.4: 'abc', 5:'deval', 9.8: 'bbasb', 9.78:'ttea', 23:'asccd', 7.9:'thy'}
print(find_max_key(data))  