from operator import  add


def split_list(input_list):

    half = len(input_list)//2

    return input_list[:half], input_list[half:]


def split_and_add(input_list):
    output = input_list.copy()
    iteration = 0

    while len(output) != 1:
        first_half, second_half = split_list(output)
        h1 = len(first_half)
        h2 = len(second_half)
        diff = abs(h1-h2)

        if h1 > h2:
            second_half = [0] * diff + second_half

        elif h2 > h1:
            first_half = [0] * diff + first_half

        output = list(map(add, first_half, second_half))
        iteration += 1

        print("step # "+str(iteration))
        print("first_half " + str(first_half))
        print("first_half " + str(second_half))
        print("output " + str(output))
        print("")

    print("Final array " + str(output))

    return output, iteration


def main():
    print("Enter the array of numbers (seperated by space) : ")
    input_list = [int(i) for i in input().split()]
    print("Input array is " + str(input_list))
    split_and_add(input_list)


if __name__ == "__main__":
    main()
