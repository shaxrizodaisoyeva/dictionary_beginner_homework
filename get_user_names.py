def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    b=[]
    for i in data:
        if i["country"]==country:
            b.append(i["name"])
    return b
data=[{'name': 'A', 'country':'USA'}, {'name': 'B', 'country':'USA'}, {'name':'C', 'country':'Uzb'}]
country="USA"
print(get_user_names(data,country))