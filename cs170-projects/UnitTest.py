"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""
from solver import *

def true(var):
    assert var, "Expected: True; Found: False"

def false(var):
    assert not var, "Expected: False; Found: True"

def equal(var1, var2):
    assert var1 == var2, "Expected: {0} == {1}; Found: they are different".format(var1, var2)

def testingDisplay(className):
    print("\n############### TESTING {0} #####################".format(className))

if __name__ == '__main__':

    # Testing Item
    testingDisplay("ITEM")
    var = Item('test', 0, 2, 1.5, 4)
    equal(var.profit, 2.5)
    equal(var.profit_per_weight_ratio(), 1.25)
    equal(var.profit_per_cost_ratio(), 2.5/1.5)
    print("TEST PASSED\n")

    # Testing Constraint
    testingDisplay("Constraint")
    var = Constraint()

    true(var.ok(1, 2))

    var.parse('1, 2, 3, 4')
    true(var.ok(1, 1))
    true(var.ok(1, 5))
    false(var.ok(2, 3))

    items = []
    # Item(name, class, weight, cost, resale)
    items.append(Item('5', 5, 0, 2, 0))
    items.append(Item('1', 1, 2, 0, 4))
    items.append(Item('6', 6, 2, 3, 0))

    true(var.valid(items))
    false(var.invalid(items))
    true(var.hasConflict(4, 3))

    var.createConflict([5, 2])
    false(var.hasConflict(3, 5))
    false(var.ok(2, 5))
    true(var.hasConflict(2, 5))
    true(var.valid(items))
    false(var.invalid(items))
    items.append(Item('2', 2, 0, 0, 0))
    false(var.valid(items))
    true(var.invalid(items))

    print("TEST PASSED\n")

    # Testing Bag
    testingDisplay("Bag")

    ## Note constraint now has conflict: (1, 2, 3, 4), (2, 5)
    bag = Bag(0, 0, var)
    true(bag.take_check(items[3]))
    false(bag.take_check(items[0]))
    bag.clear()
    bag.setM(10)
    true(bag.take_check(items[0]))
    bag.setP(2)
    true(bag.take_check(items[1]))
    false(bag.take_check(items[1]))
    bag.remove(items[1])
    bag.setP(4)
    true(bag.take_check(items[1]))
    bag.clear()
    bag.setP(100)
    bag.setM(100)
    bag.take_check(items[0])
    bag.take_check(items[2])
    true(bag.remove(items[0]))
    false(bag.remove(items[0]))
    true(bag.remove(items[2]))
    bag.clear()
    true(bag.can_take(6))
    true(bag.can_take(2))
    bag.take_check(items[0])
    false(bag.can_take(2))


    print("TEST PASSED\n")







