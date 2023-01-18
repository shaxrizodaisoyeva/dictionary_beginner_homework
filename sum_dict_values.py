def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    ''' 
    sum=0
    b=list(data.values())
    for i in b:
        sum+=i
    return sum
data={'name':2,
'age':34, 'nae':43,
'ge':34, 'nme':23,
'ae':35}
print(sum_dict_values(data))  