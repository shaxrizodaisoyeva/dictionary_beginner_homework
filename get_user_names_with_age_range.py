def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    a=0 
    b=[]
    c=[]
    d=[]
    while a<len(data):
        b+=data[a].values()
        a+=1
    c+=b[1::2]
    for i in c:
        if i in list(range(min_age,max_age+1)):
            d+=b[c.index(i)*2]
    return d
data=[{'name':"a",
'age':15}, {'name':"b",
'age':34}, {'name':"c",
'age':45}]
min_age=30
max_age=50
print(get_user_names_with_age_range(data, min_age, max_age))