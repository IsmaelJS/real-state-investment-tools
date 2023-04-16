from utils import compute_anual_cost


def test_compute_anual_cost():
    anual_cost = compute_anual_cost(170000, 10)
    assert anual_cost == 170000.0
