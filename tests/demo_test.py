from unittest import TestCase
from python_skeleton.demo import Demo


class DemoTestCase(TestCase):
    def setUp(self):
        self.demo = Demo()

    def test_hello(self):
        assert self.demo.hello("World") == "Hello, World"
