import day02
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_get_save_reports_sample(sample_list):
    assert day02.safe_report_count(sample_list) == 2

def test_get_save_reports(real_list):
    assert day02.safe_report_count(real_list) == 670

def test_get_save_reports_sample_mul(sample_list):
    assert day02.safe_report_with_mulligan(sample_list) == 4

def test_get_save_reports_mul(real_list):
    assert day02.safe_report_with_mulligan(real_list) == 694
