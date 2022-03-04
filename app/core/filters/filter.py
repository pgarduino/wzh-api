from typing import Dict

from .condition import Condition

class Filter:
    """
        Represents a set of conditions to filter data.
    """
    def __init__(self) -> None:
        """
            Constructor of filter
        """
        self.conditions = []

    def add_condition(self, condition: Condition):
        """
            to add a collection

            :param condition: The condition of filter
        """
        self.conditions.append(condition)

    def __call__(self, data = Dict) -> bool:
        """
            to evaluate all conditions of filter

            :param data: the data to evaluate
        """
        for condition in self.conditions:
            if not condition.compare(data):
                return False
        return True
