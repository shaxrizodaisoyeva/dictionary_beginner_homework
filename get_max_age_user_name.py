def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    a=0 
    b=[]
    c=[]
    while a<len(data):
        b+=data[a].values()
        a+=1
    c+=b[1::2]
    d=c.index(max(c))
    e=b[2*d]
    return e
data=[{'name':"a",
'age':34}, {'name':"b",
'age':34}, {'name':"c",
'age':35}]
print(get_max_age_user_name(data))
