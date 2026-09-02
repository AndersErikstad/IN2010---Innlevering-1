

def adam(x):
    pass



def teque(input:str):
    input_as_list = input.strip().split("\n")
    for operation in range(1, int(input_as_list[0])):
        operation_and_num = operation.split()
        x = int(input_as_list[operation][1])
        if input_as_list[operation][0] == "get":
            return
        elif input_as_list[operation][0] == "push_front":

        elif input_as_list[operation][0] == "push_middle":

        elif input_as_list[operation][0] == "push_back":
