#from math import *
initiate = True
count = 0
while initiate == True:
    count += 1

    if "7" in str(count) or "11" in str(count) or count % 7 == 0 or count % 11 == 0:
        print("klappa")
    else:
        print(count)
    

    # for counts in str(count):
    #     if("7" in counts):
    #         print("skip")
    # for counts in str(count):
    #     if("11" in counts):
    #         print("skip")


