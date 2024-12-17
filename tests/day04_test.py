import day04
from common_fixtures import sample_list, real_list


def test_get_xmases_sample(sample_list):
    assert day04.get_xmases(sample_list) == 18

def test_get_xmases(real_list):
    assert day04.get_xmases(real_list) == 2496

def test_get_masses_sample(sample_list):
    assert day04.get_mases(sample_list) == 9

def test_get_masses(real_list):
    assert day04.get_mases(real_list) == 1967
