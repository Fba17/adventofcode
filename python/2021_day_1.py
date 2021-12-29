from python.utils import read_file_2_list

input_file_name = "input_1.txt"


def main():
    input_arr = read_file_2_list(input_file_name)
    counter = 0
    array_length = len(input_arr)
    for i in range(0 , array_length):
        j = i + 1
        act = input_arr[i]
        if j < array_length:
            next_elt = input_arr[j]
            counter = counter +1 if act < next_elt else counter
    return counter


if __name__ == "__main__":
    result = main()
    print (result)