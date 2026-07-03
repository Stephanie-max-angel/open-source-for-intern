from task import subtract_numbers

def test_subtract_numbers():
  assert subtract_numbers(10, 3) == 7

def test_subtract_equal_numbers():
  assert subtract_numbers(5, 5) == 0

def test_subtract_negative_result():
  assert subtract_numbers(3, 10) == -7