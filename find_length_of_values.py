def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    a=0 
    b=[]
    sum=0
    while a<len(data):
        b+=data.values()
        sum+=len(b[a])
        a +=1
    return sum
data={'name': 'abc', 'job':'deval', 'na': 'bbasb', 'j':'ttea', 'nam':'asccd', 'jo':'thy'}
print(find_length_of_values(data)) 