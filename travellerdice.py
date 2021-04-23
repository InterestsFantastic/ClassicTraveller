from random import randint

_letternumbers = '0123456789ABCDEF'


def rd6():
    return randint(1,6)

def r2d6():
    return rd6() + rd6()

def rd66():
    return rd6() * 10 + rd6()

def coinflip():
    return randint(1,100) > 50


class Char:
    def __init__(self):
        self.gen_random()
    
    def gen_random(self):
        self.str = r2d6()
        self.dex = r2d6()
        self.end = r2d6()
        self.int = r2d6()
        self.edu = r2d6()
        self.soc = r2d6()
        
    def report(self):
        statstr = _letternumbers[self.str]
        statstr += _letternumbers[self.dex]
        statstr += _letternumbers[self.end]
        statstr += _letternumbers[self.int]
        statstr += _letternumbers[self.edu]
        statstr += _letternumbers[self.soc]

        return statstr

def testchar():
    c = Char()
    print(c.report())

def dicerolls():
    print(f'Character Gen: {Char().report()}\n')
    print('Coin Flips: ', end='')
    for x in range(10):
        print(coinflip(), end=', ')
    print('\n')

    print('1d6: ', end='')
    for x in range(30):
        print(rd6(), end=',')
    print('\n')
    
    print('2d6: ', end='')
    for x in range(20):
        print(r2d6(), end=',')
    print('\n')

    print('d66: ', end='')
    for x in range(20):
        print(rd66(), end=',')
    print('\n')

if __name__ == '__main__':
    dicerolls()

