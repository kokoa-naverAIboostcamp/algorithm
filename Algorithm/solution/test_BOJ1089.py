import glob
import pytest
from BOJ1089 import main

path = './test_BOJ1089_*.txt'
test_case = []
test_output = [8.0, 48.5, 49.5, -1]
for i, filename in enumerate(glob.glob(path)):
    with open(filename, 'r') as f:
        n = int(f.readline())
        strs = [list(inner_str) for inner_str in f.read().split('\n')]
        test_case.append((n, strs, test_output[i]))


@pytest.mark.parametrize("a, b, c", test_case)
def test_boj1089(a, b, c):
    ans = main(a, b)
    assert ans == c