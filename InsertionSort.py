import sys
from collections import deque

class InsertionSort:
    def __init__(self):
        self.array = [] # normal python lists are arrays under the hood

    def feedElement(self, element):
        self.array.append(element)

    def sort(self):
        t = 0


    def returnArray(self):
        return self.array


if __name__ == "__main__":
    ss = InsertionSort()

    rawInput = sys.stdin.read().strip().split("\n")


    for element in rawInput:
        ss.feedElement(int(element))

    ss.sort()