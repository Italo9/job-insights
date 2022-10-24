from src.counter import count_ocurrences


def test_counter():
    """A função retorna corretamente a quantidade de ocorrências da palavra
    javascript desprezando estrutura de letra maiúsculas e minúsculas"""
    result_lowercase = count_ocurrences("src/jobs.csv", "javascript")
    result_uppercase = count_ocurrences("src/jobs.csv", "Javascript")

    assert result_uppercase == result_lowercase

    """A função retorna corretamente a quantidade de ocorrências da palavra
    python desprezando estrutura de letra maiúsculas e minúsculas"""
    result_lowercase = count_ocurrences("src/jobs.csv", "python")
    result_uppercase = count_ocurrences("src/jobs.csv", "Python")

    assert result_uppercase == result_lowercase
