import numpy as np

def generate_points(diameter, num_points, angle_deg):
    angle_rad = np.radians(angle_deg)
    # Calculate radius based on the diameter
    radius = diameter / 2.0
    # Generate equally spaced distances along the line at the specified angle
    distances = np.linspace(-radius, radius, num_points)
    # Calculate x and y coordinates for each point
    x_coords = distances * np.cos(angle_rad)
    y_coords = distances * np.sin(angle_rad)

    return x_coords, y_coords

wafer_diameter = 300  
num_points = 10         
angle_degrees = 45      

# Generate equally spaced points
x_coords, y_coords = generate_points(wafer_diameter, num_points, angle_degrees)

output_file = 'equally_spaced_points1.txt'
with open(output_file, 'w') as file:
    for x, y in zip(x_coords, y_coords):
        file.write(f"({x:.4f}, {y:.4f})\n")
