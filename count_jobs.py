def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    a=data.count(job)
    return a 
data=['developer', 'teacher', 'pilot', 'developer', 'doctor', 'teacher']
job='student'
print(count_jobs(data, job))