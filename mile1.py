import numpy as np

def generate_equally_spaced_points(diameter_mm, num_points, angle_deg):
    angle_rad = np.radians(angle_deg)
    # Calculate radius based on the diameter
    radius = diameter_mm / 2.0
    # Generate equally spaced distances along the line at the specified angle
    distances = np.linspace(-radius, radius, num_points)
    # Calculate x and y coordinates for each point
    x_coords = distances * np.cos(angle_rad)
    y_coords = distances * np.sin(angle_rad)

    return x_coords, y_coords

wafer_diameter_mm = 300  # Replace with your wafer diameter
num_points = 30         # Replace with the desired number of points
angle_degrees = 0      # Replace with the desired angle

# Generate equally spaced points
x_coords, y_coords = generate_equally_spaced_points(wafer_diameter_mm, num_points, angle_degrees)

# Save the output to a text file
output_file = 'equally_spaced_points.txt'
with open(output_file, 'w') as file:
    for x, y in zip(x_coords, y_coords):
        file.write(f"({x:.4f}, {y:.4f})\n")
