import day03
from common_fixtures import sample_list, real_list


def test_get_muls_sample(sample_list):
    assert day03.get_mul(sample_list) == 161

def test_get_muls(real_list):
    assert day03.get_mul(real_list) == 166905464

def test_get_dos_sample(sample_list):
    assert day03.get_mul2(sample_list) == 48

def test_get_dos(real_list):
    assert day03.get_mul2(real_list) == 2
