"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

from __future__ import division
import argparse
from solver import *
import os

def create_solver(problem_path):
    """
    Return the solver used for the problem.
    """
    solver = Solver()
    solver.read_input(problem_path)
    return solver

def read_solution(solution_path):
    """
    Return the list of item names given in the solution file
    """
    with open(solution_path) as f:
        item_names = []
        line = f.readline()
        while line != '':
            item_names.append(line.strip())
            line = f.readline()
    return item_names

def score(solver, item_names):
    all_items = solver.items
    item_map = dict()
    total_profit = 0
    for item in all_items:
        item_map[item.name] = item
    for name in item_names:
        curr_item = item_map[name]
        if curr_item == None:
            return False
        total_profit += curr_item.profit
    return total_profit + solver.M

def improve(solver, old_solution):
    print("preprocessing data")
    old_score = score(solver, old_solution) - solver.M
    map_name_to_item = dict()
    for item in solver.items:
        map_name_to_item[item.name] = item
    items = [map_name_to_item[i] for i in old_solution]
    bag = Bag(solver.P, solver.M, solver.constraints)
    for i in items:
        bag.take(i)
    new_score = bag.value() - bag.cost()
    not_chosen = [i for i in solver.items if i not in items]
    initial = True
    print("start improving...")
    iteration = 0
    # items = get_priority_queue(items, lambda x: -x.cost)
    # not_chosen = get_priority_queue(not_chosen, lambda x: x.cost)
    # while not items.isEmpty() and not not_chosen.isEmpty():
    #     print(" progress: iteration {0}".format(iteration), end="\r")
    #     poped_item = items.pop()
    #     bag.remove(poped_item)
    #     candidate_item = not_chosen.pop()
    #     while not not_chosen.isEmpty() and bag.can_take(candidate_item.classNumber):
    #         iteration += 1
    #         if candidate_item.profit <= poped_item.profit :
    #             candidate_item = not_chosen.pop()
    #         else:
    #             bag.take(candidate_item)
    #             new_score = bag.value() - bag.cost()
    #             if new_score <= old_score:
    #                 bag.remove(candidate_item)
    #             break

    length = len(not_chosen)
    not_chosen = get_priority_queue(not_chosen, lambda x: x.profit / (0.6 * x.cost + 0.3 * x.weight))
    candidate_item = not_chosen.pop()
    while not not_chosen.isEmpty():
        if bag.can_take(candidate_item.classNumber):
            print(" progress: iteration {0:.2f}%".format(iteration / length * 100), end="\r")
            iteration += 1
            if bag.take_with_check(candidate_item):
                new_score = bag.value() - bag.cost()
                if new_score <= old_score:
                    bag.remove(candidate_item)
            else:
                bag.remove(candidate_item)
        candidate_item = not_chosen.pop()
    return bag.items()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="calculating score")
    parser.add_argument("input_file", type=str, help="____.in")
    parser.add_argument("solution_file", type=str, help="____.out")
    args = parser.parse_args()

    solver = create_solver(args.input_file)
    old_solution = read_solution(args.solution_file)

    print("before improvement: {0}".format(str(score(solver, old_solution))))
    new_solution = improve(solver, old_solution)

    if 'improved' not in os.listdir("."):
        os.mkdir("improved")

    newName = args.input_file
    if '/' in args.input_file:
        newName = newName[::-1]
        i = newName.find('/')
        newName = newName[:i][::-1]
    newName = newName.replace("in", "out")
    newName = "improved/" + newName

    solver.write_output(newName, new_solution)
    print("new file wrote to {0}".format(newName))
    print("after improvement: {0}".format(str(score(solver, [i.name for i in new_solution]))))


