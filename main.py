class PrimalNumber():
    def __init__(self, start, end) -> None:
        print(f'Prime numbers between {start} and {end} are :')

        for i in range(start, end + 1):
             isPrime = self.__getRange(i)

             if isPrime:
                  print(i)


    def __getRange(self, i):
        if i <= 1:
            return False
        if i <= 3:
            return True
        if i % 2 == 0 or i % 3 == 0:
            return False

        startNumber = 5
        while startNumber * startNumber <= i:
            if i % startNumber == 0:
                return False

            startNumber += 2

        return True

start = input('start: ')
end = input('end: ')

if (start == ''):
    start = 25

if (end == ''):
    end = 50

PrimalNumber(int(start), int(end))