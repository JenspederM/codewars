class CircularList():
    def __init__(self, *args):

        self.l = list(args)
        self.p = None

        if len(self.l) == 0:
            raise InputError("You must supply at least one item")

    def next(self):
        if self.p == None or self.p == len(self.l) - 1:
            self.p = 0
        else:
            self.p += 1

        return self.l[self.p]

    def prev(self):
        if self.p is None or self.p == 0:
            self.p = len(self.l) - 1
        else:
            self.p -= 1

        return self.l[self.p]
