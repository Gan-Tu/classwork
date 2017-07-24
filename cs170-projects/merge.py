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

def merge(solver, bad, good):

    print("preprocessing data")
    map_name_to_item = dict()
    for item in solver.items:
        map_name_to_item[item.name] = item

    bad_items = [map_name_to_item[i] for i in bad]
    good_items = [map_name_to_item[i] for i in good]

    bag = Bag(solver.P, solver.M, solver.constraints)
    for i in bad_items:
        bag.take(i)

    print("merging...")
    good_items.sort(key=lambda x: -x.profit)
    added_profit = 0
    for i, item in enumerate(good_items):
        print(" progress: {0:.2f}% with new profit {1}".format(i / len(good_items) * 100, added_profit), end="\r")
        if bag.can_take(item.classNumber) and bag.has_enough_weight_for(item.weight)\
            and bag.has_enough_money_for(item.cost):
            bag.take(item)
            added_profit += item.profit
            if bag.full():
                break
    return bag.items()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="calculating score")
    parser.add_argument("input_file", type=str, help="____.in")
    parser.add_argument("solution_file_1", type=str, help="____.out")
    parser.add_argument("solution_file_2", type=str, help="____.out")
    args = parser.parse_args()

    solver = create_solver(args.input_file)
    solution_file_1 = read_solution(args.solution_file_1)
    solution_file_2 = read_solution(args.solution_file_2)

    score1 = score(solver, solution_file_1)
    score2 = score(solver, solution_file_2)
    print("before: score {0:.3f} and {1:.3f}".format(score1, score2))

    print("merging...")
    if score1 < score2:
        new_solution = merge(solver, solution_file_1, solution_file_2)
    else:
        new_solution = merge(solver, solution_file_2, solution_file_1)

    if 'merged' not in os.listdir("."):
        os.mkdir("merged")

    newName = args.input_file
    if '/' in args.input_file:
        newName = newName[::-1]
        i = newName.find('/')
        newName = newName[:i][::-1]
    newName = newName.replace("in", "out")
    newName = "merged/" + newName

    solver.write_output(newName, new_solution)
    print("\nnew file wrote to {0}".format(newName))
    print("after improvement: {0}".format(str(score(solver, [i.name for i in new_solution]))))


