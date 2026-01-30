class animal:
    def __init__(self, x, y, energie, age, mouton):
        self.pos = (x,y)
        self.energie = energie
        self.age = age
        self.mouton = mouton #true si c'est un mouton et false si c'est un loup

    def update_energie(self, gain):
        self.energie += gain
    
    def update_age(self):
        self.age += 1

