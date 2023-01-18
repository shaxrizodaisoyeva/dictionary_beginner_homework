def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    a=0 
    b=[]
    while a<len(data):
        b+=data[a].values()
        a+=1
    c= b.count(age)
    return c
data=[{'name':"a",
'age':34}, {'name':"b",
'age':34}, {'name':"c",
'age':35}]
age=45
print(count_users_with_age(data, age))
