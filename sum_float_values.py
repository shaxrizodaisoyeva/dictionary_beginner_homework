def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    sum=0
    b=list(data.values())
    for i in b:
        if type(i)==float:
            sum+=i
    return sum
data={'name':2,
'age':34.1, 'nae':43.2,
'ge':34, 'nme':23,
'ae':35}
print(sum_float_values(data))