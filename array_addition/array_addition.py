from operator import  add


def split_list(input_list):
    """" split the input list into two different list

    Parameters
    ----------
    input_list : list
        This is the list passed to be split into two lists

    Returns : ([first_half] , [second_half])
        Returns two lists representing the first half and second half of the input

    Example:
        >>> split_list([1,2,3,4,5,6,7])
        ([1, 2, 3], [4, 5, 6, 7])
    """

    half = len(input_list)//2

    return input_list[:half], input_list[half:]


def split_and_add(input_list):
    """" split the input list into halves and add it repeatedly until a single item representing the sum remains

    Parameters
    ----------
    input_list : list
        This is the input list

    Returns : ([single_sum] , iterations)
        Returns lists representing the sum and number of iterations required to achieve it


    Example:
        >>> split_and_add([1,2,3,4,5,6,7])
        ([28], 3)
    """
    output = input_list.copy()
    iteration = 0

    while len(output) != 1:
        first_half, second_half = split_list(output)

        len_h1 = len(first_half)
        len_h2= len(second_half)
        diff = abs(len_h1-len_h2)

        # find the smaller list & left pad it with 0 for the difference
        # TODO: may be wrap this into a different function
        if len_h1 > len_h2:
            second_half = [0] * diff + second_half

        elif len_h2 > len_h1:
            first_half = [0] * diff + first_half

        output = list(map(add, first_half, second_half))
        iteration += 1

    return output, iteration


def main():
    print("Enter the array of numbers (seperated by space) : ")
    input_list = [int(i) for i in input().split()]
    print("Input array is " + str(input_list))

    output, iterations = split_and_add(input_list)

    print("Final array " + str(output))
    print("Number of Iterations = " + str(iterations))


if __name__ == "__main__":
    main()
