weight_list = []


def weight_list_creator(weight):
    weight_list.append(weight)


class Animals:
    def __init__(self, nickname, environment, food, name, weight, voice):
        self.name = name
        self.environment = environment
        self.food = food
        self.weight = weight
        self.voice = voice
        weight_list_creator(self.weight)

    def environment(self):
        print("house of {} is {}".format(self.name, self.environment))

    def voice(self):
        print("the {} say {}".format(self.name, self.voice))


class EggsGivers(Animals):

    def output(self):
        print("{} give the eggs".format(self.name))

    def feeding(self):
        print("{} are fed {}} ".format(self.name, self.food))

    def getoutput(self):
        print("from {} was got eggs ".format(self.name))


class MilkGivers(Animals):
    def output(self):
        print("{} give the milk".format(self.name))

    def feeding(self):
        print("{} are fed {}} ".format(self.name, self.food))

    def getoutput(self):
        print("from {} was got milk ".format(self.name))


class WoolGivers(Animals):
    def output(self):
        print("{} give the wool".format(self.name))

    def feeding(self):
        print("{} are fed {}} ".format(self.name, self.food))

    def getoutput(self):
        print("from {} was got wool ".format(self.name))


goose_one = EggsGivers("first_goose", "garden", "grain", "goose", 123, "ga")
goose_two = EggsGivers("second_goose", "garden", "grain", "goose", 321, "ga")

cow = MilkGivers("single_cow", "grassland", "grass or straw", "cow", 1234, "moo")

sheep_one = WoolGivers("first_sheep", "grassland", "grass or straw", "sheep", 1234, "me")
sheep_two = WoolGivers("second_sheep", "grassland", "grass or straw", "sheep", 1234, "me")

chicken_one = EggsGivers("first_chicken", "garden", "grain", "chicken", 24, "coco")
chicken_two = EggsGivers("second_chicken", "garden", "grain", "chicken", 27, "coco")

goat_one = WoolGivers("first_goat", "grassland", "grass or straw", "goat", 1234, "be")
goat_two = WoolGivers("second_goat", "grassland", "grass or straw", "goat", 1234, "be")

duck = EggsGivers("single_duck", "garden", "grass or straw", "duck", 15, "quack")

print("summarize weight is {}".format(sum(weight_list)))
print("maximum weight is {}".format(max(weight_list)))
