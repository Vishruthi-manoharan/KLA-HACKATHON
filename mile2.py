import numpy as np

def generate_die_indices_and_llc(wafer_diameter, die_size_x, die_size_y, die_shift_vector, cow_to_reference_die, output_file):
    die_indices_llc = []

    # Calculate the number of dies in x and y directions
    num_dies_x = int(np.ceil(wafer_diameter / die_size_x))
    num_dies_y = int(np.ceil(wafer_diameter / die_size_y))

    # Open the output file for writing
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

                
                file.write(f"({i},{j}):({round(llc_x, 4)},{round(llc_y, 4)})\n")

    return die_indices_llc


wafer_diameter = 300
die_size_x, die_size_y = 30, 30
die_shift_vector = (0, 0)
cow_to_reference_die = (15, 15)
output_file = 'die_indices_llc.txt'

result = generate_die_indices_and_llc(wafer_diameter, die_size_x, die_size_y, die_shift_vector, cow_to_reference_die, output_file)
