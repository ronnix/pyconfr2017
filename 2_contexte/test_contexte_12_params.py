"""
Combinaison de fixtures paramétrées de py.test
"""
import pytest


def moyenne(nombres):
    return sum(nombres) / len(nombres)


@pytest.fixture(params=[list, tuple, set])
def type_collection(request):
    return request.param


@pytest.fixture(ids=['croissant', 'decroissant'], params=[
    [1, 2, 3, 4],
    [4, 3, 2, 1],
])
def valeurs_collection(request):
    return request.param


def test_moyenne(type_collection, valeurs_collection):
    nombres = type_collection(valeurs_collection)
    assert moyenne(nombres) == 2.5
