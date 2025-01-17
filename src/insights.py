from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    filter_job_type = []
    for row in result:
        if row["job_type"] not in filter_job_type:
            filter_job_type.append(row["job_type"])

    return filter_job_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)
    return filter_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    result = read(path)
    filter_industry = []
    for row in result:
        if row["industry"] not in filter_industry and row["industry"] != "":
            filter_industry.append(row["industry"])
    return filter_industry


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_industry_type = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry_type.append(job)
    return filter_industry_type


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    result = read(path)
    result_salary_int = []
    result_salary_max = int
    for row in result:
        if row["max_salary"].isdigit():
            result_salary_int.append(int(row["max_salary"]))
            result_salary_max = max(result_salary_int)
    return result_salary_max


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    result = read(path)
    result_salary_int = []
    result_salary_min = int
    for row in result:
        if row["min_salary"].isdigit():
            result_salary_int.append(int(row["min_salary"]))
            result_salary_min = min(result_salary_int)
    return result_salary_min


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Valor fora do intervalo")
    elif not (isinstance(job["min_salary"], int)) or (
        not isinstance(job["max_salary"], int) or not isinstance(salary, int)
    ):
        raise ValueError("Valores fora do conjunto dos inteiros")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Valor minimo maior que valor maximo")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filter_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_by_salary.append(job)
        except ValueError as Error:
            print(Error)
    return filter_by_salary
