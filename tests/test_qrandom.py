import pytest
from src.qrandom.qrandom import randint


def test_randint():
    assert type(randint(0,2)), int
