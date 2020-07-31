position_first = input("enter the first position (num<space>num) ")
position_second = input("enter the end position (num<space>num) ")

try:
    if int(position_second.split(' ')[0]) > 8 or \
            int(position_second.split(' ')[1]) > 8 or \
            int(position_first.split(' ')[0]) > 8 or \
            int(position_first.split(' ')[1]) > 8:
        print("illegal nums, you must use only nums 1 - 8 ")
        exit()

    print("yes" if int(position_second.split(' ')[0]) - int(position_first.split(' ')[0]) ==
                   int(position_second.split(' ')[1]) - int(position_first.split(' ')[1])
          else "no")

except ValueError:
    print("probably you use words, you must use only nums 1 - 8")
