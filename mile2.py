import math

def generate_die_indices_and_llc(wafer_diameter, die_size_x, die_size_y, die_shift_vector, cow_to_reference_die, output_file):
    die_indices_llc = []

    # Calculate the number of dies in x and y directions
    num_dies_x = math.ceil(wafer_diameter / die_size_x)
    num_dies_y = math.ceil(wafer_diameter / die_size_y)

    with open(output_file, 'w') as file:
        # Iterate over all dies
        for i in range(num_dies_x):
            for j in range(num_dies_y):
                # Calculate die index
                die_index = (i, j)

                # Calculate LLC in wafer coordinate
                llc_x = i * die_size_x + die_shift_vector[0] + cow_to_reference_die[0]
                llc_y = j * die_size_y + die_shift_vector[1] + cow_to_reference_die[1]

                # Ensure LLC coordinates are within the wafer diameter
                llc_x = max(0, min(wafer_diameter - die_size_x, llc_x))
                llc_y = max(0, min(wafer_diameter - die_size_y, llc_y))

                # Append die index and LLC to the list
                die_indices_llc.append((die_index, (round(llc_x, 4), round(llc_y, 4))))

                # Write die index and LLC to the text file
                file.write(f"({i},{j}):({round(llc_x, 4)},{round(llc_y, 4)})\n")

    return die_indices_llc

# Example usage
wafer_diameter_1 = 300
die_size_x_1, die_size_y_1 = 30, 30
die_shift_vector_1 = (0, 0)
cow_to_reference_die_1 = (15, 15)
output_file_1 = 'die_indices_llc_1.txt'

wafer_diameter_2 = 200
die_size_x_2, die_size_y_2 = 10, 10
die_shift_vector_2 = (10, 10)
cow_to_reference_die_2 = (25, 25)
output_file_2 = 'die_indices_llc_2.txt'

wafer_diameter_3 = 300
die_size_x_3, die_size_y_3 = 24, 70
die_shift_vector_3 = (5, 38)
cow_to_reference_die_3 = (-7, 3)
output_file_3 = 'die_indices_llc_3.txt'

wafer_diameter_4 = 300
die_size_x_4, die_size_y_4 = 2, 2
die_shift_vector_4 = (15, 15)
cow_to_reference_die_4 = (-44, -66)
output_file_4 = 'die_indices_llc_4.txt'

result_1 = generate_die_indices_and_llc(wafer_diameter_1, die_size_x_1, die_size_y_1, die_shift_vector_1, cow_to_reference_die_1, output_file_1)
result_2 = generate_die_indices_and_llc(wafer_diameter_2, die_size_x_2, die_size_y_2, die_shift_vector_2, cow_to_reference_die_2, output_file_2)
result_3 = generate_die_indices_and_llc(wafer_diameter_3, die_size_x_3, die_size_y_3, die_shift_vector_3, cow_to_reference_die_3, output_file_3)
result_4 = generate_die_indices_and_llc(wafer_diameter_4, die_size_x_4, die_size_y_4, die_shift_vector_4, cow_to_reference_die_4, output_file_4)


