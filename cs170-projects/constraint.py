"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

class Constraint:

    def __init__(self):
        self.table = dict()

    def __str__(self):
        string = ""
        for series in self.table:
            string += "conflict class: {0}, {1}\n".format(\
                            str(series), str(self.table[series]))
        return string

    def parse(self, line):
        """
        Parse a line of numbers representing mutually exclusive classes, 
        separated by comma. For example, '12, 23, 42' means items of 
        class 12, 23, and 42 cannot be put together. 
        This method does NOT perform validation on input format.
        """
        numbers = list(eval(line))
        self.createConflict(numbers)

    def createConflict(self, incompatibles):
        """
        Add constraints to this object that items of class numbers 
        specified by INCOMPATIBLES array cannot be put together.
        """
        if len(incompatibles) != len(set(incompatibles)):
            raise ValueError("a class cannot be incompatible with itself.\n" + str(incompatibles))
        for n in incompatibles:
            if n not in self.table:
                self.table[n] = set()
            for n2 in incompatibles:
                if n != n2:
                    self.table[n].add(n2)

    def hasConflict(self, class1, class2):
        """
        Return true iff class1 and class2 has conflict and cannot be put together
        """
        if class1 not in self.table:
            return False
        return class2 in self.table[class1]

    def ok(self, class1, class2):
        """
        Return true iff class1 and class2 has no conflict and can be put together
        """
        return not self.hasConflict(class1, class2)

    def valid(self, items):
        """
        Return true iff all items of classes listed in ITEMS
        have no conflict with each other and can be put together
        """
        items = list(items)
        end = len(items)
        if end <= 0:
            return True
        for i in range(end):
            for j in range(i, end):
                if self.hasConflict(items[i].classNumber, items[j].classNumber):
                    return False
        return True

    def invalid(self, items):
        """
        Return true iff all items of classes listed in ITEMS
        have any conflict with each other and cannot be put together
        """
        return not self.valid(items)



