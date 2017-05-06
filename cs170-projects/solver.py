"""
Spring 2017 CS170 Final Project
@author Gan Tu
"""

#!/usr/bin/env python

from __future__ import print_function, division
import argparse
from item import Item
from bag import Bag
from constraint import Constraint
from util import *
from random import random, sample, shuffle

class Solver:

    def __init__(self):
        self.initialized = False
        self.filename = "uninitialized solver"
        self.solution = None

    ############################ I/O METHODS ############################

    def read_input(self, filename):
        """
        P: float
        M: float
        N: integer
        C: integer
        items: list of tuples
        constraints: list of sets

        Return true iff this process finished successfully
        """
        with open(filename) as f:
            self.P = float(f.readline())
            self.M = float(f.readline())
            self.N = int(f.readline())
            self.C = int(f.readline())
            self.items = []
            self.map_name_to_items = dict()
            self.constraints = Constraint()
            self.raw_constraints = list() # this is constraints without modification
            for i in range(self.N):
                name, cls, weight, cost, val = f.readline().split(";")
                item = Item(name, int(cls), float(weight), float(cost), float(val))
                self.items.append(item)
                self.map_name_to_items[name] = item
            for i in range(self.C):
                one_list_of_constraint = eval(f.readline())
                self.constraints.createConflict(one_list_of_constraint)
                self.raw_constraints.append(one_list_of_constraint)

        self.initialized = True
        self.filename = filename
        return True

    def output_solution(self):
        import os
        if 'output' not in os.listdir("."):
            os.mkdir('output')
        if self.solution is None:
            raise RuntimeError("hasn't found a solution yet")
        return self.write_output(self.filename.replace('in','out'), self.solve())

    def write_output(self, filename, items_chosen):
        with open(filename, "w") as f:
            for i in items_chosen:
                f.write("{0}\n".format(i.name))
        return True

    def solve(self, resolve=False):
        """
        Run our algorithm, save and return the solution.
        It will return saved solution from now on and 
        return it in future unless RESOLVE is false.
        If you want to resolve the problem, set RESOLVE to True.

        This is different from run_algorithm for this doesn't solve anything
        but only deals with the logistic issues.
        """
        if not self.initialized:
            raise RuntimeError("solver hasn't been initialized with input problem.")

        if resolve or self.solution is None:
            # WE DECLARE A SEPARATE ALGORITHMIC CALL TO MAKE OUR IMPLMENTATION CLEAN.
            self.solution = self.run_algorithm()
        return self.solution

    def run_algorithm(self):
        """
        Solve the problem using algorithm and return the items chosen for the solution.
        """
        raise NotImplementedError

class GreedySolver(Solver):

    def run_algorithm(self, num_solution_before_stop=100000, time_out=1000000):
        """
        This is where we implement our logic and algorithms

        Useful Parameters:
        self.P -- max weight we can carry
        self.M -- max purchasing power in dollars
        self.N -- total number of avaliable items
        self.C -- total number of constraints
        self.items -- all items avaliable for choice
        self.constraints -- a Constraint class with constraints
        """

        # STEP: Create a hashmap from class number to its items
        item_map = dict()
        for item in self.items:
            if item.classNumber not in item_map:
                item_map[item.classNumber] = set()
            item_map[item.classNumber].add(item)

        # STEP: Calculate the total weight, cost, value, and profit of each class
        def get_class_stats(items):
            total_weight = 0
            total_cost = 0
            total_value = 0
            total_profit = 0
            for item in items:
                total_weight += item.weight
                total_cost += item.cost
                total_value += item.value
                total_profit += item.profit
            return (total_weight, total_cost, total_value, total_profit)

        class_stats = dict() # Format: key: class -> value: (weight, cost, value, profit)
        for classNumber in item_map.keys():
            class_stats[classNumber] = get_class_stats(item_map[classNumber])

        # STEP: Create a BAG instance
        bag = Bag(self.P, self.M, self.constraints)

        # STEP: PriorityQueues of class's values

        fn_extract_profit_per_weight_ratio = lambda x: x.profit_per_weight_ratio()
        
        def fn_extractclass_ratio(x):
            weight, _, _, profit = class_stats[x]
            if weight == 0:
                ratio = float("inf")
            else:
                ratio = profit / weight
            return ratio


        class_queue = PriorityQueue(lowest_priority=False) # based on class's item profit_per_weight_ratio
        for classNumber in item_map.keys():
            class_queue.push(classNumber, fn_extractclass_ratio(classNumber))

        def add_to_queue(items, fn_extract_priority, queue):
            for item in items:
                priority_value = fn_extract_priority(item)
                queue.push(item, -priority_value)
            return queue

        def get_queue_of_items(items, fn_extract_priority):
            queue = PriorityQueue(lowest_priority=False)
            return add_to_queue(items, fn_extract_priority, queue)


        # STEP: pick from the bag with highest ratio
        solutions_found = dict()
        num_solution_found = 0
        iteration = 0

        class_not_used_due_to_conflict = Queue()

        add_back_conflicts = True

        while num_solution_found <= num_solution_before_stop and iteration <= time_out:
            while not class_queue.isEmpty() and iteration <= time_out:
                iteration += 1
                if iteration % (time_out / 1000) == 0:
                    print("iteration {0} -- rate: {1:.2f} %".format(iteration, iteration / time_out * 100), end="\r")
                if not class_not_used_due_to_conflict.isEmpty():
                    class_to_use  = class_not_used_due_to_conflict.pop()
                    add_back_conflicts = not add_back_conflicts
                else: 
                    class_to_use = class_queue.pop()
                    add_back_conflicts = not add_back_conflicts
                if bag.can_take(class_to_use):
                    items_queue = get_queue_of_items(item_map[class_to_use], \
                                                fn_extract_profit_per_weight_ratio)
                    item = items_queue.pop()
                    while bag.take(item):
                        if not items_queue.isEmpty():
                            item = items_queue.pop()
                        else:
                            break
                    num_solution_found += 1
                    solutions_found[bag.score()] =  bag.items()
                    print("solution {0} found".format(num_solution_found))
                else:
                    class_not_used_due_to_conflict.push(class_to_use)
                if num_solution_found >= num_solution_before_stop:
                    break
            # print("iteration {0}".format(iteration))
            iteration += 1
            if add_back_conflicts:
                add_to_queue(class_not_used_due_to_conflict.list, fn_extractclass_ratio, class_queue)
            if num_solution_found >= num_solution_before_stop:
                break

        # STEP: return the best combination found
        bestSolution = []
        bestProfit = 0
        for profit, soln in solutions_found.items():
            if profit > bestProfit:
                bestProfit = profit
                bestSolution = soln
        return bestSolution

class HybridGreedySolver(Solver):

    def greedy_on_fn(self, priority_fn, lowestPriority=False):
        solution = list()
        total_profit = 0
        bag = Bag(self.P, self.M, self.constraints)
        queue = get_priority_queue(self.items, priority_fn, lowestPriority)
        
        while not queue.isEmpty() and not bag.full():
            item = queue.pop()
            #print(" remaining items: {0:.2f}%".format(queue.count / self.N * 100), end="\r")
            print(" progress: {0:.2f} %".format(max(bag._weight / bag.P, bag._cost/bag.M) * 100), end="\r")
            if bag.has_enough_weight_for(item.weight) and bag.has_enough_money_for(item.cost):
                if bag.can_take(item.classNumber):
                    solution.append(item)
                    bag.take(item)
                    total_profit += item.profit
        return (total_profit, solution)

    def greedy_on_min_weight(self):
        return self.greedy_on_fn(lambda x: x.weight, lowestPriority=True)

    def greedy_on_max_profit(self):
        return self.greedy_on_fn(lambda x: x.profit)

    def greedy_on_profit_per_weight_ratio(self):
        return self.greedy_on_fn(lambda x: x.profit_per_weight_ratio())

    def greedy_on_profit_per_cost_ratio(self):
        return self.greedy_on_fn(lambda x: x.profit_per_cost_ratio())

    def greedy_on_profit_per_cost_weight_combined_ratio(self):
        return self.greedy_on_fn(lambda x: x.profit_per_cost_weight_combined_ratio())

    def randomized_select(self, select_range, priority_fn, lowestPriority=False):
        solution = list()
        total_profit = 0
        bag = Bag(self.P, self.M, self.constraints)
        options = list()
        for item in self.items:
            options.append((item, priority_fn(item)))
        options.sort(key=lambda x: -x[1])
        if lowestPriority:
            options = list(reversed(options))
        options = [x[0] for x in options]

        while len(options) > 0 and not bag.full():
            items = options[:min(select_range, len(options))]
            item = items[int(random() * len(items))]
            options.remove(item)
            print(" progress: {0:.2f} %".format(max(bag._weight / bag.P, bag._cost/bag.M) * 100), end="\r")
            if bag.has_enough_weight_for(item.weight) and bag.has_enough_money_for(item.cost):
                bag.take(item)
                solution.append(item)
                total_profit += item.profit
                new_options = list()
                for x in options:
                    if bag.can_take(x.classNumber):
                        new_options.append(x)
                options = new_options
        return (total_profit, solution)

    def randomized_select_on_profit_per_cost_ratio(self, select_range=10):
        return self.randomized_select(select_range, lambda x: x.profit_per_cost_ratio())

    def randomized_select_on_profit_per_weight_ratio(self, select_range=10):
        return self.randomized_select(select_range, lambda x: x.profit_per_weight_ratio())

    def randomized_select_on_min_weight(self, select_range=10):
        return self.randomized_select(select_range, lambda x: x.weight, lowestPriority=True)

    def randomized_select_on_max_profit(self, select_range=10):
        return self.randomized_select(select_range, lambda x: x.profit)

    def run_algorithm(self):
        solutions = list()
        print("\nmethod 1:")
        solutions.append(self.greedy_on_profit_per_weight_ratio())
        print("\nmethod 2:")
        solutions.append(self.randomized_select_on_profit_per_cost_ratio())
        print("\nmethod 3:")
        solutions.append(self.randomized_select_on_profit_per_cost_ratio(3))
        print("\nmethod 4:")
        solutions.append(self.randomized_select_on_profit_per_weight_ratio())
        print("\nmethod 5:")
        solutions.append(self.randomized_select_on_profit_per_weight_ratio(3))

        solution = max(solutions, key=lambda x: x[0])
        return solution[1]

class GoogleSolver(Solver):

    def run_algorithm(self):

        from ortools.algorithms import pywrapknapsack_solver
        solver = pywrapknapsack_solver.KnapsackSolver(\
                    pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,\
                    'solver')
        # Scaling Items
        epsilon = 0.3
        print("Scaling items for {0}-epsilon approximation".format(epsilon))
        # Randomly select a group of non-conflict items to do knapsack on:
        print("Randomly select a group of items that have no conflicts")
        items = self.compatible_items_random(self.N)

        # Preprocess Data
        print("Preprocess Data")
        weights = list()
        values = list()
        capacities = list()
        map_indicies_to_item = dict()

        item_costs = list()
        item_weights = list()

        max_profit = max([x.profit for x in self.items])
        scaling_factor = self.N / epsilon / max_profit
        print("Scaling factor: {0}".format(scaling_factor))

        for i, item in enumerate(items):
            values.append(min(item.profit * scaling_factor, 0))
            item_weights.append(item.weight)
            item_costs.append(item.cost)
            map_indicies_to_item[i] = item

        # Form Knapsack problem
        print("Creating Knapsack problem")

        weights.append(item_costs)
        capacities.append(self.M)

        weights.append(item_weights)
        capacities.append(self.P)

        # Initialize Solver
        solver.Init(values, weights, capacities)

        # Solve
        print("Solving...")
        picked = solver.Solve()
        print("Done!")

        # Retrieve solution
        print("Converting solution to items...")

        packed_items_indices = [x for x in range(0, len(weights[0])) if solver.BestSolutionContains(x)]
        packed_items = [map_indicies_to_item[x] for x in packed_items_indices]

        print("Success!")
        return packed_items

    def compatible_items_random(self, N, select_range=20):
        solution = list()
        options = list()

        map_class_to_items = dict()
        
        for item in self.items:
            if item.classNumber not in map_class_to_items:
                map_class_to_items[item.classNumber] = set()
            map_class_to_items[item.classNumber].add(item)

        map_class_to_ppw_ratio = dict()
        for num, items in map_class_to_items.items():
            map_class_to_ppw_ratio[num] = sum([x.profit for x in items]) / (sum([x.weight for x in items]) + 0.01)
        options = list(map_class_to_ppw_ratio.keys())
        options.sort(key=lambda x: -map_class_to_ppw_ratio[x])
        
        while len(options) > 0 and len(solution) < N:
            numbers = options[:min(select_range, len(options))]
            num = numbers[int(random() * len(numbers))]
            options.remove(num)
            print(" selection progress: {0:.2f} %".format(len(solution) / N * 100), \
                    end="\r")
            solution.extend(map_class_to_items[num])
            new_options = list()
            for x in options:
                if self.constraints.ok(x, num):
                    new_options.append(x)
            options = new_options
        return solution

class GurobiSolver(Solver):

    def run_algorithm(self):
        from gurobipy import Model, GRB
        model = Model("NP-Hard")

        print("Setting Model Parameters")
        # set timeout
        model.setParam('TimeLimit', 1600)
        model.setParam('MIPFocus', 3)
        model.setParam('PrePasses', 1)
        model.setParam('Heuristics', 0.01)
        model.setParam('Method', 0)

        map_name_to_item = dict()
        map_name_to_cost = dict()
        map_name_to_weight = dict()
        map_name_to_profit = dict()
        map_class_to_name = dict()
        
        item_names = list()

        print("Preprocessing data for model...")

        for item in self.items:
            item_names.append(item.name)
            map_name_to_item[item.name] = item
            map_name_to_cost[item.name] = item.cost
            map_name_to_weight[item.name] = item.weight
            map_name_to_profit[item.name] = item.profit
            if item.classNumber not in map_class_to_name:
                map_class_to_name[item.classNumber] = list()
            map_class_to_name[item.classNumber].append(item.name)

        class_numbers = list(map_class_to_name.keys())

        print("Setting model variables...")
        # binary variables =1, if use>0
        items = model.addVars(item_names, vtype=GRB.BINARY, name="items")
        classes = model.addVars(class_numbers, vtype=GRB.BINARY, name="class numbers")

        print("Setting model objective...")
        # maximize profit
        objective = items.prod(map_name_to_profit)
        model.setObjective(objective, GRB.MAXIMIZE)

        # constraints
        print("Setting model constraints")
        model.addConstr(items.prod(map_name_to_weight) <= self.P,"weight capacity")
        model.addConstr(items.prod(map_name_to_cost) <= self.M,"cost capacity")
        
        # if any item from a class is chosen, that class variable has to be a binary of 1
        for num in class_numbers:
            model.addGenConstrOr(classes[num], [items[x] for x in map_class_to_name[num]] ,name="class count")

        for c in self.raw_constraints:
            count = model.addVar()
            for n in c:
                if n in classes:
                    count += classes[n]
            model.addConstr(count <= 1, name="constraint")

        print("Start optimizing...")
        model.optimize()
        print("Done! ")

        # Status checking
        status = model.Status
        if status == GRB.Status.INF_OR_UNBD or \
           status == GRB.Status.INFEASIBLE  or \
           status == GRB.Status.UNBOUNDED:
            print('The model cannot be solved because it is infeasible or unbounded')

        if status != GRB.Status.OPTIMAL:
            print('Optimization was stopped with status ' + str(status))
            Problem = True

        try:
            model.write("mps_model/" + self.filename + ".sol")
        except Exception as e:
            pass

        print("Generating solution file...")
        # Display solution
        solution_names = list()
        for i, v in enumerate(items):
            if items[v].X > 0.9:
                solution_names.append(item_names[i])

        solution = [map_name_to_item[x] for x in solution_names]
        return solution

class ScaledGurobiSolver(Solver):

    def run_algorithm(self):

        old_M = self.M
        old_items = [i.copy() for i in self.items]
        map_name_to_old_item = dict()
        for i in old_items:
            map_name_to_old_item[i.name] = i
        self.scale_items_by_cost()

        from gurobipy import Model, GRB
        model = Model("NP-Hard")

        print("Setting Model Parameters")
        # set timeout
        model.setParam('TimeLimit', 1600)
        model.setParam('MIPFocus', 3)
        model.setParam('PrePasses', 1)
        model.setParam('Heuristics', 0.01)
        model.setParam('Method', 0)

        map_name_to_item = dict()
        map_name_to_cost = dict()
        map_name_to_weight = dict()
        map_name_to_profit = dict()
        map_class_to_name = dict()
        
        item_names = list()

        print("Preprocessing data for model...")

        for item in self.items:
            item_names.append(item.name)
            map_name_to_item[item.name] = item
            map_name_to_cost[item.name] = item.cost
            map_name_to_weight[item.name] = item.weight
            map_name_to_profit[item.name] = item.profit
            if item.classNumber not in map_class_to_name:
                map_class_to_name[item.classNumber] = list()
            map_class_to_name[item.classNumber].append(item.name)

        class_numbers = list(map_class_to_name.keys())

        print("Setting model variables...")
        # binary variables =1, if use>0
        items = model.addVars(item_names, vtype=GRB.BINARY, name="items")
        classes = model.addVars(class_numbers, vtype=GRB.BINARY, name="class numbers")

        print("Setting model objective...")
        # maximize profit
        objective = items.prod(map_name_to_profit)
        model.setObjective(objective, GRB.MAXIMIZE)

        # constraints
        print("Setting model constraints")
        model.addConstr(items.prod(map_name_to_weight) <= self.P,"weight capacity")
        model.addConstr(items.prod(map_name_to_cost) <= self.M,"cost capacity")
        
        # if any item from a class is chosen, that class variable has to be a binary of 1
        for num in class_numbers:
            model.addGenConstrOr(classes[num], [items[x] for x in map_class_to_name[num]] ,name="class count")

        for c in self.raw_constraints:
            count = model.addVar()
            for n in c:
                if n in classes:
                    count += classes[n]
            model.addConstr(count <= 1, name="constraint")

        print("Start optimizing...")
        model.optimize()
        print("Done! ")

        # Status checking
        status = model.Status
        if status == GRB.Status.INF_OR_UNBD or \
           status == GRB.Status.INFEASIBLE  or \
           status == GRB.Status.UNBOUNDED:
            print('The model cannot be solved because it is infeasible or unbounded')

        if status != GRB.Status.OPTIMAL:
            print('Optimization was stopped with status ' + str(status))
            Problem = True

        try:
            model.write("mps_model/" + self.filename + ".sol")
        except Exception as e:
            pass

        print("Generating solution file...")
        # Display solution
        solution_names = list()
        for i, v in enumerate(items):
            try:
                if items[v].X > 0.9:
                    solution_names.append(item_names[i])
            except Exception as e:
                pass

        self.M = old_M
        self.items = old_items
        solution = [map_name_to_old_item[i] for i in solution_names]
        return solution

    def scale_items_by_cost(self):
        discard = set()
        min_cost = min([x.cost for x in self.items])
        from math import log
        scaling_factor = 10 ** log(abs(min_cost) + 1) / 10 + 1
        self.M = self.M / scaling_factor
        print("Scaling factor: {0}".format(scaling_factor))
        for item in self.items:
            if item.weight > self.P:
                discard.add(item)
            else:
                item.cost = item.cost / scaling_factor
                item.calculate_ratio()
        for trash in discard:
            self.items.remove(trash)


