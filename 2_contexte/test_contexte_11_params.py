"""
Les fixtures paramétrées de py.test
"""
import pytest


def moyenne(nombres):
    return sum(nombres) / len(nombres)


@pytest.fixture(params=[list, tuple, set])
def nombres(request):
    type_collection = request.param
    return type_collection([1, 2, 3, 4])


def test_moyenne(nombres):
    assert moyenne(nombres) == 2.5
