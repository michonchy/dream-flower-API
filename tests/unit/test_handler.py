import json

import pytest

from dream_flower import app


def test_is_dream_flower():
    assert app.is_dream_flower(1) == '''とんでとんでとんでとんでとんでとんでとんでとんでとんでまわってまわってまわってまわる
'''
