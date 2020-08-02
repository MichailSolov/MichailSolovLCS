boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print(list(zip(sorted(boys), sorted(girls))) if len(boys) == len(girls) else "кто-то может остаться без пары!")

