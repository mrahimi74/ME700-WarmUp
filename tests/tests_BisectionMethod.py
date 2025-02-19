import numpy as np
from BisectionMethod import bisection as BM
import pytest

def test_avg_x_y():
  x = 10
  y = 20
  assert np.isclose(BM.Avg(x, y), 15)

def test_sign():
  x = 12
  assert np.isclose(BM.sign(x), 1)
  x = -4
  assert np.isclose(BM.sign(x), -1)

def test_abs():
  x = 19
  assert np.isclose(BM.abs(x), 19)
  x = -241
  assert np.isclose(BM.abs(x), 241)
  
def test_check():
  x = 12
  y = 17
  assert BM.check(x,y) == True
  x = 5
  y = 3
  with pytest.raises(ValueError, match = f"Invalid input: {x} is greater than {y}."):
    BM.check(x,y)
  

f = lambda x: x**2 - 12

def test_opps_sign():
  x = 3
  y = 5
  assert BM.opps_sign(x, y, f) == True
  x = 5
  y = 3
  with pytest.raises(ValueError, match = "f(a) and f(b) must have opposite signs"):
    BM.opps_sign(x,y)


g = lambda x: x ** 3 + 5
def test_bisection():
  p,q,r = BM.bisection(-3, 1, 200, 1e-11, g)
  assert np.isclose(p, -1.7099759466764226)
  with pytest.raises("Solution did not converge as the maximum iteration reached"):
    p,q,r = BM.bisection(-3, 1, 2, 1e-11, g)