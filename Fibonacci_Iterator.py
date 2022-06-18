import unittest

import parameterized


class Fibonacci:
  def __init__(self, n):
    self.limit = n
    self.preceding_1 = 0
    self.preceding_2 = 1
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0:
      self.index += 1
      return 0
    if self.index == self.limit:
      raise StopIteration()
    result = self.preceding_1 + self.preceding_2
    self.preceding_2, self.preceding_1 = self.preceding_1, result
    self.index += 1
    return result

class FibonacciV2:
  def __init__(self, n):
    self.limit = n
    self.a = 0
    self.b = 1
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index < self.limit:
      result = self.a
      self.a, self.b = self.b, self.a + self.b
      self.index += 1
      return result
    else:
      raise StopIteration


class FibonacciTest(unittest.TestCase):
  @parameterized.parameterized.expand([(1, (0,)), (2, (0, 1)), (5, (0, 1, 1, 2, 3))])
  def test_something(self, limit, expected):
    fin = Fibonacci(limit)
    self.assertSequenceEqual(list(x for x in iter(fin)), expected)  # add assertion here


class FibonacciTestV2(unittest.TestCase):
  @parameterized.parameterized.expand([(1, (0,)), (2, (0, 1)), (5, (0, 1, 1, 2, 3))])
  def test_something(self, limit, expected):
    fin = FibonacciV2(limit)
    self.assertSequenceEqual(list(x for x in iter(fin)), expected)  # add assertion here

if __name__ == '__main__':
  unittest.main()
