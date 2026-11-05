import time
import pytest

@pytest.fixture
def beifan():
    print("用例之前")

    s = time.time()
    yield s

    print("用例之后")