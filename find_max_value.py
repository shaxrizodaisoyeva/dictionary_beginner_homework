def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    a=0 
    b=[]
    while a<len(data):
        b+=data.values()
        a +=1
    c= max(b)
    return c
data={3.4: 34, 5:45, 9.8:45, 9.78:67, 23:54, 7.9:43}
print(find_max_value(data)) 