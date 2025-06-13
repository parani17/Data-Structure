import os

for i in range(1, 8):
    print("\n### Week {}".format(i))
    for j, k in enumerate(os.listdir("Week {}".format(i))):
        print("[REC_DS using C_Week_{}_COD_Question {}](Week%20{}/0{}.pdf)".format(i, j + 1, i, j + 1))
