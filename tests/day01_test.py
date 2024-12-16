import day01
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_get_distance_sample(sample_list):
    assert day01.get_distance(sample_list) == 11

def test_get_distance(real_list):
    assert day01.get_distance(real_list) == 1223326

def test_get_similarity_score_sample(sample_list):
    assert day01.get_similarities(sample_list) == 31

def test_get_similarity_score(real_list):
    assert day01.get_similarities(real_list) == 21070419
