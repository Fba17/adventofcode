from python.utils import read_file_2_list

input_file_name = "input_2.txt"


class Element:
    def __init__(self, elt_str: str):
        elt_array = elt_str.split(" ")
        self.step = elt_array[0]
        self.amount = int (elt_array[1])

    def is_forward(self):
        return self.step == "forward"

    def is_depth_up(self):
        return self.step == "up"

    def is_depth_down(self):
        return self.step == "down"


def main():
    input_arr = read_file_2_list(input_file_name)
    list_of_element = [Element(x) for x in input_arr]
    sum_forward = 0
    sum_up = 0
    sum_down = 0
    aim = 0
    depth = 0
    for elt in list_of_element:
        sum_forward = sum_forward + elt.amount if elt.is_forward() else sum_forward
        sum_up = sum_up + elt.amount if elt.is_depth_up() else sum_up
        sum_down = sum_down + elt.amount if elt.is_depth_down() else sum_down
        if elt.is_forward() and aim > 0:
            depth = depth + (aim * elt.amount)
        if elt.is_depth_down():
            aim = aim + elt.amount
        if elt.is_depth_up():
            aim = aim - elt.amount

    return sum_forward * depth


if __name__ == '__main__':
    result = main()
    print(result)
