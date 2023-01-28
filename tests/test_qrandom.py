import pytest
from qoalas.src.qrandom.qrandom import randint


@pytest.fixture
def test_randint():
    assert type(randint()), int
