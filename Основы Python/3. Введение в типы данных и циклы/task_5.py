import operator

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

print(max(stats.items(), key=operator.itemgetter(1))[0])
