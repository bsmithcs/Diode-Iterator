#
# Brayden Smith
# 3/12/2026
#
# Series Diode Circuit Simulation
# Diode Voltage/Current via Iterative Method
#

import math

# CONSTANTS

I_S = 1e-17 # Amperes
V_T = 0.0259 # Volts

# CALCULATION

print("\n            -----Beginning Series Diode Simulation-----\n\nEnter reasonable values below to determine Diode Voltage/Current\nvia the Iterative Method")

while True:
    # Get circuit conditions
    print("\n")
    R = float(input("Resistance in the circuit? "))
    V_S = float(input("Supply voltage? "))
    numDiodes = int(input("Number of series diodes? "))
    print("\n")

    topLine = "  -----"
    for i in range(0, numDiodes):
        topLine += ">|"
        if (i+1) != numDiodes:
            topLine += "--"
    topLine += "-----"
    print(topLine)
    spaces = " " * (6 + 4*(numDiodes))
    print(" +|" + spaces + "|")
    print("  O" + spaces + "Z")
    print(" -|" + spaces + "|")
    bottomLine = "  -----"
    if numDiodes == 1:
        bottomLine += "-------"
    else:
        bottomLine += (numDiodes-1) * "----" + "-------"
    print(bottomLine + "\n")

    # Start with guess of 0.7 Volts for V_D
    V_D = 0.7
    I_D = -9999

    for i in range(5):
        if I_D == -9999:
            print(f"{i}\tV_D: {V_D:.3f} V\tI_D: -")
        elif I_D >= 1:
            print(f"{i}\tV_D: {V_D:.3f} V\tI_D: {I_D:.3f} A")
        elif I_D >= 0.001:
            print(f"{i}\tV_D: {V_D:.3f} V\tI_D: {I_D*1000:.3f} mA")
        else:
            print(f"{i}\tV_D: {V_D:.3f} V\tI_D: {I_D*1000000:.3f} uA")

        I_D = (numDiodes*V_D + V_S) / R
        V_D = V_T * math.log(I_D / I_S)

