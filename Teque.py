from pyarrow import nulls


def adam(x):
    pass

# Tenker vi lager vår egen liste?
class LinkedList:
    def __init__(self):


class Node:
    def __init__(self, content, next: 'Node'):
        self.content = content
        self.next = next
    def get_content(self):
        return self.content
    def get_next(self):
        return self.next


def teque(input:str):

    input_as_list = input.strip().split("\n")
    for operation in range(1, int(input_as_list[0])):
        operation_and_num = operation.split()
        x = int(input_as_list[operation][1])
        if input_as_list[operation][0] == "get":

        elif input_as_list[operation][0] == "push_front":

        elif input_as_list[operation][0] == "push_middle":

        elif input_as_list[operation][0] == "push_back":
