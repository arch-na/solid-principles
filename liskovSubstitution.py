class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

def make_bird_fly(bird):
    print(bird.fly())

sparrow = Sparrow()
make_bird_fly(sparrow)
