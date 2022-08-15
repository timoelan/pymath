from pythagoras import calculate_A, calculate_h, calculate_c, calculate_a, calculate_b, calculate_c_from_h_and_A


def test_calculate_h():
    assert calculate_h(20, 10) == 4


def test_calculate_c_from_h_and_A():
    assert calculate_c_from_h_and_A(10, 20) == 1.0


def test_calculate_b():
    assert calculate_b(10, 20) == 17.320508075688775


def test_calculate_a():
    assert calculate_a(10, 20) == 17.320508075688775


def test_calculate_A():
    assert calculate_A(10, 20) == 100.0


def test_calculate_c():
    assert calculate_c(10, 20) == 22.360679774997898
