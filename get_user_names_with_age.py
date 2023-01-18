def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    a=0 
    b=[]
    for i in data:
         if i["age"]==age:
            b.append(i["name"])
    return b
data=[{'name':"a",
'age':34}, {'name':"b",
'age':32}, {'name':"c",
'age':32}]
age=32
print(get_user_names_with_age(data, age))
 
