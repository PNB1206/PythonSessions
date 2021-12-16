class Test:
    input=[23,65,19,90,56]
    print(input)
    #Swap any 2 numbers from a list
    def swapBySimple(self, input):
        p1,p2 =1,4
        self.input[p1],self.input[p2] = self.input[p2],self.input[p1]
        print(self.input)

    def swapingByPopFunction(self, input):
        p1,p2 = 0,3
        first_ele = self.input.pop(p1)
        sec_ele = self.input.pop(p2-1)

        self.input.insert(p1,sec_ele)
        self.input.insert(p2,first_ele)
        print(self.input)


    def swapByUsingTuple(self, l):
        p1,p2 = 2,4
        get = (l[p1], l[p2])
        l[p2],l[p1] = get
        print(l)





t = Test()
#t.swapBySimple(input)
#t.swapingByPopFunction(input)
t.swapByUsingTuple(t.input)