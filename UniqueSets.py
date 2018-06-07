class Unique():
    def __init__(self, intList):
        self._ints = intList


    def returnUniqueInts(self):
        setsOfLists = []
        while True:
            temp = []
            for i in self._ints:
                if i not in setsOfLists:




        return setsOfLists


print(Unique([4,5,6]).returnUniqueInts())
