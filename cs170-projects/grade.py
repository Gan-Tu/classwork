"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

from __future__ import division
import argparse
from solver import *

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

def score(problem_path, solution_path):
    solver = create_solver(problem_path)
    item_names = read_solution(solution_path)
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


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="calculating score")
    parser.add_argument("input_file", type=str, help="____.in")
    parser.add_argument("solution_file", type=str, help="____.out")
    args = parser.parse_args()

    print("{0}: ".format(args.solution_file) + str(score(args.input_file, args.solution_file)))


