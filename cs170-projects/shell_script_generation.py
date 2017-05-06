import os

if 'shell' not in os.listdir("."):
    os.mkdir("shell")

# string = "python solver.py input/problem{0}.in\n"
# with open("shell/solve_all.sh", "w") as file:
#     for i in range(1, 22):
#         file.write(string.format(i))
# os.system("chmod +x shell/solve_all.sh")

# string = "python grade.py input/problem{0}.in output/problem{0}.out \n"
# with open("shell/grade_all.sh", "w") as file:
#     for i in range(1, 22):
#         file.write(string.format(i))
# os.system("chmod +x shell/grade_all.sh")

# string = "python autograder.py input/problem{0}.in output/problem{0}.out \n"
# with open("shell/verify_all.sh", "w") as file:
#     for i in range(1, 22):
#         file.write(string.format(i))
# os.system("chmod +x shell/verify_all.sh")

# string1 = "python grade.py input/problem{0}.in compare/1/problem{0}.out\n"
# string2 = "python grade.py input/problem{0}.in compare/2/problem{0}.out\n"
# with open("shell/compare_all.sh", "w") as file:
#     for i in range(1, 22):
#         file.write(string1.format(i))
#         file.write(string2.format(i))
# os.system("chmod +x shell/compare_all.sh")

# string = "python grade.py input/problem{0}.in ../submission/4/problem{0}.out \n"
# with open("shell/grade_all.sh", "w") as file:
#     for i in range(1, 22):
#         file.write(string.format(i))
# os.system("chmod +x shell/grade_all.sh")

string1 = "python merge.py input/problem{0}.in output/problem{0}.out output/submission/problem{0}.out\n"
string2 = "python autograder.py input/problem{0}.in merged/problem{0}.out\n"
string3 = "python grade.py input/problem{0}.in merged/problem{0}.out\n"
with open("shell/merge_all.sh", "w") as file:
    for i in [3,11,14,16,17,18,20]:
        file.write(string1.format(i))
        file.write(string2.format(i))
        file.write(string3.format(i))
os.system("chmod +x shell/merge_all.sh")

