import pytest
from typing import Union, List
import numpy as np
from app import bubblesort


test = [([4,5,3,2,7,6,9,1,8],[1,2,3,4,5,6,7,8,9]),
        ([3,2,7,8,9,1,4,6,5],[1,2,3,4,5,6,7,8,9])]

# Faza 1 - test do sorotowania bąbelkowego
@pytest.mark.parametrize('sample, expected_list', test)
def test_bubblesort(sample,expected_list):
    got = bubblesort(sample)
    want = expected_list
    assert got == want

test_2 = [(['4','5','3','2','7','6','9','1','8'],np.NaN),
            ([3,2,7,8,9,1,4,6,5],[1,2,3,4,5,6,7,8,9])]


# Faza 1 - dodanie nowyego testu
@pytest.mark.parametrize('sample, expected_list', test)
def test_bubblesort_2(sample,expected_list):
    if np.any(np.isnan(expected_list)):
        got = bubblesort(sample)
        want = expected_list
        assert type(got) == type(want)
    else:
        got = bubblesort(sample)
        want = expected_list
        assert got == want
    
