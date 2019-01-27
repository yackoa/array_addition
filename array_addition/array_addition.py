
def split_list(input_list):

    half = len(input_list)//2

    return input_list[:half], input_list[half:]


def main():
    print("Enter the array of numbers (seperated by space) : ")
    input_list = [int(i) for i in input().split()]
    print("Input array is " + str(input_list))


if __name__ == "__main__":
    main()
