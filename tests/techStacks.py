# -*- coding: utf-8 -*-


import unittest
from ddt import ddt, data, unpack
import logging

from stacks import TriangularStack, OverflowException, WRONG_INDEX_ERROR_STRING, WaterNotFilledException

__author__ = "julianadamwise@gmail.com"
LOGGER = logging.getLogger(__name__)


@ddt
class TriangularStackTests(unittest.TestCase):
    """
    Testing class for TriangularStack class
    """

    def setUp(self):
        """
        setup of default stack
        """
        self.rows = 7
        self.unit_capacity = 0.250
        self.defaultStack = TriangularStack(size=self.rows,
                                            unit_capacity=self.unit_capacity)

    def test_triangular_stack_initialized_properly(self):
        "Base test"
        self.assertIsInstance(self.defaultStack, TriangularStack)
        self.assertEqual(self.rows, self.defaultStack.size)
        self.assertEqual(self.unit_capacity, self.defaultStack.unit_capacity)

    @data((4, 2), (5, 1), (2, 0.450), (1, 0.250))
    @unpack
    def test_pouring_water_in_stack_when_capacity_is_higher(self, size, k_liter_water):
        "Test pouring water"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=self.unit_capacity)
        self.assertTrue(triangular_stack.pour(k_liter_water))


    @data((4, 1, 10), (5, 0.25,3.75), (0, 10, 0))
    @unpack
    def test_maximun_capacity_of_stack(self, size, capacity, max_size):
        "Test calculation of maximum size to throw sane errors"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=capacity)
        self.assertEqual(triangular_stack.maximum_water_limit, max_size)


    @data((4, 6), (5, 9), (2, 7), (1, 1.250))
    @unpack
    def test_pouring_water_in_stack_when_capcity_is_lower_and_overflows(self, size, k_liter_water):
        "Test pouring water"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=self.unit_capacity)
        with self.assertRaises(OverflowException):
            triangular_stack.pour(k_liter_water)
