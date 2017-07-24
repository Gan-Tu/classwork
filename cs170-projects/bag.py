"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

P_UPPER_BOUND = 2**32
M_UPPER_BOUND = 2**32

class Bag:
    
    def __init__(self, P, M, constraints, name="bag"):
        """
        Construct a bag that can contain at most P pounds and M dollars

        Args:
            P: the max total weight of items that this bag can handle
            M: the max total cost of items that this bag can contain
            constraints: a class of constraints
            name: the name of this bag
        """
        assert P < P_UPPER_BOUND, "P (weight) can not be larger than 2^32"
        assert M < M_UPPER_BOUND, "M (value) can not be larger than 2^32"
        self.P = P
        self.M = M
        self.name = name
        self._cost = 0
        self._value = 0
        self._weight = 0
        self._items = set()
        self._class_numbers_contained = list()
        self._quick_class_conflict_check = set()
        self._constraints = constraints

    ############################ BASIC METHODS ############################
    def setP(self, P):
        """
        Set the weight limit to P.
        """
        assert P < P_UPPER_BOUND, "P (weight) can not be larger than 2^32"
        self.P = P

    def setM(self, M):
        """
        Set the money limit to M.
        """
        assert M < M_UPPER_BOUND, "M (value) can not be larger than 2^32"
        self.M = M

    def setName(self, name):
        """
        Set the bag name to NAME.
        """
        self.name = name

    def setConstraint(self, constraints):
        """
        Set the constraints for the bag to be CONSTRAINTS
        """
        self.constraints = constraints

    def score(self):
        return self._value + self.M - self._cost

    def value(self):
        """
        Return the total value in this bag
        """
        return self._value

    def weight(self):
        """
        Return the total weight in this bag
        """
        return self._weight

    def cost(self):
        """
        Return the total cost in this bag
        """
        return self._cost

    def items(self):
        """
        Return the list of all the items in this bag

        WARNING: the returned list is MUTABLE!
        """
        return self._items

    def constraints(self):
        """
        Return the constraints for this bag

        WARNING: the returned list is MUTABLE!
        """
        return self._constraints

    def clear(self):
        """
        Remove all items from the bag
        """
        self._cost = 0
        self._value = 0
        self._weight = 0
        self._items = set()
        self._class_numbers_contained = list()

    ############################ USEFUL METHODS ############################
    def take(self, item):
        """
        Put ITEM in the bag. 

        Return True if the attempt is successful.
        Return False if the attempt is invalid.
        """
        self._weight += item.weight
        self._value += item.value
        self._cost += item.cost
        self._items.add(item)
        self._class_numbers_contained.append(item.classNumber)
        return True

    def take_with_check(self, item):
        """
        Put ITEM in the bag. 

        Return True if the attempt is successful.
        Return False if the attempt is invalid.
        """
        if item in self._items:
            return False
        self._items.add(item)
        if self._constraints.invalid(self._items):
            self._items.remove(item)
            return False
        self._items.remove(item)
        if self._weight + item.weight > self.P:
            return False
        if self._cost + item.cost > self.M:
            return False
        self._weight += item.weight
        self._value += item.value
        self._cost += item.cost
        self._items.add(item)
        self._class_numbers_contained.append(item.classNumber)
        return True
    
    def remove(self, item):
        """
        Remove ITEM in the bag.

        Return True if the item was removed.
        Return False if the item was not in the bag.
        """
        if item not in self._items:
            return False
        self._items.remove(item)
        self._class_numbers_contained.remove(item.classNumber)
        self._weight -= item.weight
        self._value += item.value
        self._cost -= item.cost
        for i in self._constraints.table[item.classNumber]:
            if i in self._quick_class_conflict_check:
                self._quick_class_conflict_check.remove(i)
        return True

    def can_take(self, classNumber):
        """
        Return true iff items of classNumber doesn't conflict with anything in the bag.
        """
        if classNumber in self._quick_class_conflict_check:
            return False
        for number in self._class_numbers_contained:
            if self._constraints.hasConflict(number, classNumber):
                self._quick_class_conflict_check.add(classNumber)
                return False
        return True

    def full(self):
        return self._cost >= self.M or self._weight >= self.P

    def has_enough_weight_for(self, weight):
        return self._weight + weight <= self.P

    def has_enough_money_for(self, price):
        return self._cost + price <= self.M

