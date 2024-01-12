import math

def generate_points(wafer_diameter, N, angle_deg, output_file):
    points = []
    
    # Convert angle from degrees to radians
    angle_rad = math.radians(angle_deg)
    
    # Calculate the angle between each point
    delta_angle = 2 * math.pi / N
    
    for i in range(N):
        # Calculate the coordinates of each point
        x = wafer_diameter / 2 * math.cos(angle_rad + i * delta_angle)
        y = wafer_diameter / 2 * math.sin(angle_rad + i * delta_angle)
        
        # Append the coordinates to the list of points
        points.append((round(x, 4), round(y, 4)))
    
    # Write points to the text file
    with open(output_file, 'w') as file:
        for point in points:
            file.write(f"{point}\n")

wafer_diameter = 200  
N = 25  # Replace with the desired number of points
angle_deg = 250  # Replace with the desired angle in degrees
output_file = 'generated_points.txt'  # Replace with the desired output file name

generate_points(wafer_diameter, N, angle_deg, output_file)
