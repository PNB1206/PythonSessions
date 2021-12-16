class Test:
    fruit = 'Apple'
    def rev(self, s):
        output = ''
        for ch in s:
            if ch not in output:
                output = output+ ch
        print(output)


t = Test()
t.rev(t.fruit)