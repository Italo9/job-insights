import csv

from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf8") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        group_by_department = []
        for row in jobs:
            group_by_department.append(row)
    return group_by_department
