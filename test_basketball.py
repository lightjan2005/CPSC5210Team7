from unittest import TestCase

import basketball


class TestBasketball(TestCase):
    def test_add_points(self):
        BasketballObj = basketball.Basketball()
        BasketballObj.add_points(0, 2)
        self.assertEqual(2, BasketballObj.score[0])

