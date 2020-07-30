db = [["январь", "козерог", "19"],
      ["февраль", "водолей", "19"],
      ["март", "рыбы", "20"],
      ["апрель", "овен", "20"],
      ["май", "телец", "20"],
      ["июнь", "близнецы", "20"],
      ["июль", "рак", "22"],
      ["август", "лев", "22"],
      ["сентябрь", "дева", "22"],
      ["октябрь", "весы", "22"],
      ["ноябрь", "скорпион", "22"],
      ["декабрь", "стрелец", "21"]]

birthday = input("enter the num and enter the month (emp: num<space>month) ")

for x in db:
    if birthday.split(' ')[0] <= x[2] and birthday.split(' ')[1].lower() in x:
        print(x[1])
    elif birthday.split(' ')[1].lower() in x:
        try:
            print(db[db.index(x) + 1][1])
        except IndexError:
            print("козерог")
