position_first = input("enter the first position (num<space>num) ")
position_second = input("enter the end position (num<space>num) ")

print("yes" if int(position_second.split(' ')[0]) - int(position_first.split(' ')[0]) ==
               int(position_second.split(' ')[1]) - int(position_first.split(' ')[1])
      else "no")
