from python.utils import read_file_2_list

input_file_name = "input_3.txt"


class BinaryNumbers:
    def __init__(self, numb: str):
        bit_arr = list(numb)
        self.first_bit = bit_arr[0]
        self.second_bit = bit_arr[1]
        self.third_bit = bit_arr[2]
        self.fourth_bit = bit_arr[3]
        self.fifth_bit = bit_arr[4]


def __get_other__(bit: str):
    return "0" if bit == "1" else "1"


def __get_most_appear_bit__(bit_array: list):
    amount_of_0 = 0
    amount_of_1 = 0
    for bit in bit_array:
        if bit == "0":
            amount_of_0 = amount_of_0 + 1
        else:
            amount_of_1 = amount_of_1 + 1

    return "0" if amount_of_0 > amount_of_1 else "1"


def __get_potency__(pos):
    if pos == 0:
        return 1
    else:
        result = 2
        for i in range(1, pos):
            result = result * 2
        return result


def __get_decimal_from_binary__(bit_str: str):
    bit_arr = list(bit_str)
    length = len(bit_arr) - 1
    dec_value = 0
    for i in range(0, len(bit_arr)):
        pos = length - i
        val = int(bit_arr[i]) * __get_potency__(pos)
        dec_value = dec_value + val
    return dec_value


def main():
    input_arr = read_file_2_list(input_file_name)
    list_of_binaryNumbers = [BinaryNumbers(x) for x in input_arr]
    list_of_first_bit = [bn.first_bit for bn in list_of_binaryNumbers]
    list_of_second_bit = [bn.second_bit for bn in list_of_binaryNumbers]
    list_of_third_bit = [bn.third_bit for bn in list_of_binaryNumbers]
    list_of_fourth_bit = [bn.fourth_bit for bn in list_of_binaryNumbers]
    list_of_fifth_bit = [bn.fifth_bit for bn in list_of_binaryNumbers]
    gamma_first = __get_most_appear_bit__(list_of_first_bit)
    ep_first = __get_other__(gamma_first)
    gamma_second = __get_most_appear_bit__(list_of_second_bit)
    ep_second = __get_other__(gamma_second)
    gamma_third = __get_most_appear_bit__(list_of_third_bit)
    ep_third = __get_other__(gamma_third)
    gamma_fourth = __get_most_appear_bit__(list_of_fourth_bit)
    ep_fourth = __get_other__(gamma_fourth)
    gamma_fifth = __get_most_appear_bit__(list_of_fifth_bit)
    ep_fifth = __get_other__(gamma_fifth)
    gamma_rate_bin = gamma_first + gamma_second + gamma_third + gamma_fourth + gamma_fifth
    epsilon_rate_bin = ep_first + ep_second + ep_third + ep_fourth + ep_fifth
    gamma_rate_dec = __get_decimal_from_binary__(gamma_rate_bin)
    epsilon_rate_dec = __get_decimal_from_binary__(epsilon_rate_bin)
    return gamma_rate_dec * epsilon_rate_dec


if __name__ == '__main__':
    result = main()
    print(result)
