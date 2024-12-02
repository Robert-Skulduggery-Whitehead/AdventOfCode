def input(file_name):
    input = {"left":[], "right":[]} 
    with open(file_name, 'r') as input_file:
        for line in input_file:
            x = line.split()
            input["left"].append(x[0])
            input["right"].append(x[1])
        #input.left.append()
    return input

