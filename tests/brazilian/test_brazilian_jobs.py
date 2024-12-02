from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result_job = read_brazilian_file("src/jobs.csv")
    for job in result_job:
        assert (
            (job.keys() is "titulo")
            and (job["salario"] is True)
            and (job["tipo"] is True)
        )
