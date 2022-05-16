import pytest
import requests

class TestPhrase:
    def testPhrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase)<15, f"the phrase is longer than 15 characters"
