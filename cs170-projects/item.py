"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

class Item:
 
    def __init__(self, name, classNumber, weight, cost, value):
        """
        Create an item called NAME belonging to CLASSNUMBER that weighs WEIGHT pounds,
        has a cost of COST dollars, and can be resold at RESALE dollars
        """
        self.name = name
        self.classNumber = classNumber
        self.weight = weight
        self.cost = cost
        self.value = value
        self.calculate_ratio()

    def profit_per_weight_ratio(self):
        return self._profit_per_weight_ratio

    def profit_per_cost_ratio(self):
        return self._profit_per_cost_ratio

    def profit_per_cost_weight_combined_ratio(self):
        return self._profit_per_cost_weight_combined_ratio

    def __str__(self):
        return "item {0} in class {1} with weight {2}, cost {3}, and resale value of {4}".format(self.name, self.classNumber, \
                        self.weight, self.cost, self.value)

    def calculate_ratio(self):
        self.profit = self.value - self.cost
        if self.weight != 0:
            self._profit_per_weight_ratio = self.profit / self.weight
        else:
            self._profit_per_weight_ratio = float('inf')

        if self.cost != 0:
            self._profit_per_cost_ratio = self.profit / self.cost
        else:
            self._profit_per_cost_ratio = float('inf')
            
        if self.cost != 0 and self.weight != 0:
            self._profit_per_cost_weight_combined_ratio = self.profit / self.cost / self.weight
        else:
            self._profit_per_cost_weight_combined_ratio = float('inf') 

    def copy(self):
        return Item(self.name, self.classNumber, self.weight, self.cost, self.value)
        
