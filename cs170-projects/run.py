from solver import *

greedysolver = GreedySolver()
hybridsolver = HybridGreedySolver()
gurobisolver = GurobiSolver()
googlesolver = GoogleSolver()
scaledgurobi = ScaledGurobiSolver()

################################## END ALGORITHM ##################################

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="PickItems solver.")
    parser.add_argument("input_file", type=str, help="____.in")
    parser.add_argument("--no-output", action="store_true")
    parser.add_argument("--google", action="store_true")
    parser.add_argument("--gurobi", action="store_true")
    parser.add_argument("--greedy", action="store_true")
    parser.add_argument("--hybrid", action="store_true")
    parser.add_argument("--scaled", action="store_true")
    args = parser.parse_args()

    if args.greedy:
        solver = greedysolver
    elif args.gurobi:
        solver = gurobisolver
    elif args.hybrid:
        solver = hybridsolver
    elif args.scaled:
        solver = scaledgurobi
    else:
        solver = googlesolver

    print("Reading input...")
    if solver.read_input(args.input_file):
        solution = solver.solve()
        print("\n######## Solution is: ########\n")
        total_profit = 0
        for item in solution:
            # print(item.name)
            total_profit += item.profit
        print("total profit earned: {0}".format(total_profit + solver.M))
        if not args.no_output:
            if solver.output_solution():
                print("solution wrote to {0}".format(args.input_file.replace("in", "out")))
            else:
                print("ERROR: wrote solution file unsuccessfully")

        print("\n#############################\n")
    else:
        print("ERROR: read input file unsuccessfully")