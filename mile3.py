import math

def generate_die_indices_and_llc(wafer_diameter, die_size_x, die_size_y, die_shift_vector, cow_to_reference_die,
                                  num_dies_rows, num_dies_columns, reticle_street_width, reticle_street_height,
                                  die_street_width, die_street_height, output_file):
    die_indices_llc = []

    # Calculate the total reticle size including streets
    total_reticle_width = num_dies_columns * (die_size_x + reticle_street_width) - reticle_street_width
    total_reticle_height = num_dies_rows * (die_size_y + reticle_street_height) - reticle_street_height

    # Calculate the number of dies in x and y directions
    num_dies_x = math.floor((wafer_diameter + reticle_street_width) / (die_size_x + reticle_street_width))
    num_dies_y = math.floor((wafer_diameter + reticle_street_height) / (die_size_y + reticle_street_height))

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Iterate over all dies
        for i in range(num_dies_x):
            for j in range(num_dies_y):
                # Calculate die index
                die_index = (i, j)

                # Calculate LLC in wafer coordinate
                llc_x = i * (die_size_x + reticle_street_width) + die_shift_vector[0] + cow_to_reference_die[0]
                llc_y = j * (die_size_y + reticle_street_height) + die_shift_vector[1] + cow_to_reference_die[1]

                # Ensure LLC coordinates are within the wafer diameter
                llc_x = max(0, min(wafer_diameter - total_reticle_width, llc_x))
                llc_y = max(0, min(wafer_diameter - total_reticle_height, llc_y))

                # Append die index and LLC to the list
                die_indices_llc.append((die_index, (round(llc_x, 4), round(llc_y, 4))))

                # Write die index and LLC to the text file
                file.write(f"({i},{j}):({round(llc_x, 4)},{round(llc_y, 4)})\n")

    return die_indices_llc

# Example usage
wafer_diameter = 300
die_size_x, die_size_y = 5, 5
die_shift_vector = (27, 39)
cow_to_reference_die = (43.1, 24.9)
num_dies_rows, num_dies_columns = 4, 6
reticle_street_width, reticle_street_height = 3.2, 4.2
die_street_width, die_street_height = 1.8, 1.2
output_file = 'die_indices_llc_reticle.txt'

result = generate_die_indices_and_llc(wafer_diameter, die_size_x, die_size_y, die_shift_vector, cow_to_reference_die,
                                      num_dies_rows, num_dies_columns, reticle_street_width, reticle_street_height,
                                      die_street_width, die_street_height, output_file)

