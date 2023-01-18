def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    a=0 
    b=[]
    while a<len(data):
        b+=data[a].values()
        a+=1
    c=b.index(name)
    d=b[c+1]
    return d
data=[{'name': 'A', 'country':'USA'}, {'name': 'B', 'country':'UK'}, {'name':'C', 'country':'Uzb'}]
name='d'
print(get_user_country(data, name))