from replication import compute_trend

def test_growing():
    assert compute_trend([1, 2, 3, 4]) == "growing"

def test_recovering():
    assert compute_trend([5, 4, 3, 2]) == "recovering"