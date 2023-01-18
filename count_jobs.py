def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    a=0 
    b=[]
    while a<len(data):
        b+=data[a].values()
        a+=1
    c= b.count(job)
    return c
data=[{'name': 'a', 'job':'developer'}, {'name': 'b', 'job':'teacher'}, {'name':'c', 'job':'teacher'}]
job='teacher'
print(count_jobs(data, job))