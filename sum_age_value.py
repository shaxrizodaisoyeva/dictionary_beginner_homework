def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    a=0 
    b=[]
    c=[]
    sum=0
    while a<len(data):
        b+=data[a].values()
        a+=1
    c=b[1::2]
    for i in c:
        sum+=i
    return sum
data=[{'name':"a",
'age':34}, {'name':"b",
'age':34}, {'name':"c",
'age':35}]
print(sum_age_values(data)) 