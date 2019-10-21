#!/usr/bin/python env

__author__ = 'David Poslt'

class nasobky:

    def __init__(self, hodnota, words1, words2, words3):

        self.hodnota = hodnota

        self.words1 = words1
        self.words2 = words2
        self.words3 = words3


    def multiple(self,first_nasobek, second_nasobek):
        self.first_nasobek = first_nasobek
        self.second_nasobek = second_nasobek

        for i in range(0,self.hodnota):
            if i == 0:
                print('NONE')
            elif i % self.first_nasobek == 0 and i % self.second_nasobek == 0:
                print('{}'.format(self.words3))

            elif i % self.first_nasobek == 0:
                print('{}'.format(self.words1))

            elif i % self.second_nasobek == 0:
                print('{}'.format(self.words2))

            else:
                print(i)


if __name__ == '__main__':
    n1 = nasobky(35,'Python','genius','I love python')
    n1.multiple(3,5)

