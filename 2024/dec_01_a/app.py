import time


def get_indata(file_name: str):
    with open(file_name, "r") as file:
        return file.read()


def calculate_discrepancy(data: str):
    coordinates_left = []
    coordinates_right = []
    discrepancy = 0
    lines = data.split("\n")
    for line in lines:
        coordinates_left.append(int(line.split("   ")[0]))
        coordinates_right.append(int(line.split("   ")[1]))
    coordinates_left.sort()
    coordinates_right.sort()
    for index in range(len(lines)):
        discrepancy += abs(coordinates_right[index] - coordinates_left[index])
    return discrepancy


def main():
    file_definitions = ("test_data.txt", "indata.txt")
    expected_test_result = 11

    start_time = time.time()
    print(f"Calculating...\n")

    test_data = get_indata(file_definitions[0])
    test_result = calculate_discrepancy(test_data)
    print("Test Result:", test_result)
    print("-Expected--:", expected_test_result)

    data = get_indata(file_definitions[1])
    result = calculate_discrepancy(data)
    print("Real Result:", result)

    stop_time = time.time()
    elapsed_time = round(stop_time - start_time, 3)
    print(f"\nElapsed time: {elapsed_time}s")


main()