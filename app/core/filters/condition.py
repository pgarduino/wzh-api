from typing import Dict

class Condition:
    """
        Represents a condition to filter data.
    """
    def __init__(self, field, value, operator='equal') -> None:
        """
            Constructor of condition to filter data.

            :param field: the field name of condition
            :param value: the field value of condition
            :param operator: the operator of condition (equal or contains)
        """
        self.field = field
        self.value = value
        self.operator = operator

    def compare(self, data = Dict) -> bool:
        """
            compare the condition with the data

            :param data: the data to compare
        """
        if self.field not in data:
            return False
        if self.operator == 'equal':
            return self.value == data[self.field]
        if self.operator == 'contains':
            return self.value in data[self.field]
        return False
