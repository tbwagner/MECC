import csv
import re
import matplotlib.pyplot as plt
import math

def getOutput(FILENAME):
    total_output = 0

    with open(f"data/{FILENAME}", "r") as file:
        csv_reader = csv.reader(file)
        for _ in range(14):
            next(csv_reader)
        for row in csv_reader:
            value = abs(float(row[2]))
            if value < 1:
                total_output += value ** 2
    
    return math.sqrt(total_output / 200000)

def getFilename(test_run_name):
    pattern = r'([a-zA-Z_]+)(\d+)'
    match = re.search(pattern, test_run_name)

    if match:
        name = match.group(1)
        number = match.group(2)
        if name == "Parallel":
            return f"ParallelGen_Test_Run{number}.csv"
        elif name == "Perp":
            return f"PerpGen_Test_Run{number}.csv"
        elif name == "Trig":
            return f"TrigGen_Test_Run{number}.csv"
        elif name == "Rod_Perp":
            return f"Rod_Perp_Test_Run{number}.csv"
        elif name == "Perp_LW_":
            return f"Perp_LW_Run{number}.csv"
        else:
            print("Error invalid regex test run name: " + name)
            exit(1)
    else:
        print("Error unmatched regex")
        exit(1)

frequencies = {}

with open("data/Test Summary Sheet(Input - Output Calculator).csv") as file:
    csv_reader = csv.reader(file)
    for _ in range(20):
        next(csv_reader)
    count = 0
    for row in csv_reader:
        test_run_name = row[0]
        frequency = float(row[14])
        frequencies[test_run_name] = frequency
        
        count+=1
        if count > 91:
            break

xs_parallel = []
ys_parallel = []
for i in range(1, 16):
    if i == 10:
        continue
    test_run_name = "Parallel" + str(i)
    xs_parallel.append(1/frequencies[test_run_name])
    ys_parallel.append(getOutput(getFilename(test_run_name)))

plt.plot(xs_parallel, ys_parallel, 'o', label="Parallel")


xs_perpendicular = []
ys_perpendicular = []
for i in range(16, 33):
    if i in (24, 27, 30):  
        continue
    test_run_name = "Perp" + str(i)
    xs_perpendicular.append(1/frequencies[test_run_name])
    ys_perpendicular.append(getOutput(getFilename(test_run_name)))

plt.plot(xs_perpendicular, ys_perpendicular, 'o', label="Perpendicular")


xs_triangular = []
ys_triangular = []
for i in range(33, 49):
    if i == 39:  
        continue
    test_run_name = "Trig" + str(i)
    xs_triangular.append(1/frequencies[test_run_name])
    ys_triangular.append(getOutput(getFilename(test_run_name)))

plt.plot(xs_triangular, ys_triangular, 'o', label="Triangular")

plt.xlabel("Period (s)")
plt.ylabel("RMS of Total Output (V)")
plt.title("Plot of Period (s) vs RMS of Total Output (V)")
plt.legend()
plt.show()


xs_rodperp = []
ys_rodperp = []
for i in range(49, 65):
    if i == 60:  
        continue
    test_run_name = "Rod_Perp" + str(i)
    xs_rodperp.append(1/frequencies[test_run_name])
    ys_rodperp.append(getOutput(getFilename(test_run_name)))

plt.plot(xs_rodperp, ys_rodperp, 'o', label="Rod")

plt.plot(xs_perpendicular, ys_perpendicular, 'o', label="Spring")

plt.xlabel("Period (s)")
plt.ylabel("RMS of Total Output (V)")
plt.title("Plot of Period (s) vs RMS of Total Output (V)")
plt.legend()
plt.show()


xs_rodperplw = []
ys_rodperplw = []
for i in range(65, 92):
    if i in range(68, 80):  
        continue
    test_run_name = "Perp_LW_" + str(i)
    xs_rodperplw.append(1/frequencies[test_run_name])
    ys_rodperplw.append(getOutput(getFilename(test_run_name)))

plt.plot(xs_rodperplw, ys_rodperplw, 'o', label="Light Weight")

plt.plot(xs_perpendicular, ys_perpendicular, 'o', label="Heavy Weight")

plt.xlabel("Period (s)")
plt.ylabel("RMS of Total Output (V)")
plt.title("Plot of Period (s) vs RMS of Total Output (V)")
plt.legend()
plt.show()