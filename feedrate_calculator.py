# © 2024 Joaquin Frangi. All rights reserved.
# Licensed under the BSD 3-Clause License.

import difflib

# Read the first G-code file
with open('insert your file name', 'r') as file1:
    first_gcode = file1.readlines()

# Read the second G-code file
with open('insert your file name here', 'r') as file2:
    second_gcode = file2.readlines()

print("Files read successfully.")
print("Comparing files...")

# Compare the two G-code files and store the differences
differences = list(difflib.unified_diff(first_gcode, second_gcode))
print("Comparison completed.")

print("Extracting relevant differences...")

# Keywords associated with extrusion commands
extrusion_keywords = ["M104", "M109", "M140", "M190", "M106", "G1", "M82", "M83"]

# Keywords associated with purging commands
purging_keywords = ["M106", "M107", "G92", "G10", "G11"]

# Lists to store relevant differences related to extrusion and purging
extrusion_differences = []
purging_differences = []

# Filter the differences based on keywords
for diff in differences:
    if any(keyword in diff for keyword in extrusion_keywords):
        extrusion_differences.append(diff)
    if any(keyword in diff for keyword in purging_keywords):
        purging_differences.append(diff)

print("Extraction of differences completed.")

print("Extracting feed rates...")

# Lists to store feed rates from the first and second G-code files
first_gcode_feed_rates = []
second_gcode_feed_rates = []

# Extract feed rates from the differences
for diff in extrusion_differences:
    if diff.startswith("-G1"):
        # First G-code file differences
        parts = diff.split()
        for part in parts:
            if part.startswith("F"):
                try:
                    first_gcode_feed_rates.append(float(part[1:]))
                except ValueError:
                    continue
    elif diff.startswith("+G1"):
        # Second G-code file differences
        parts = diff.split()
        for part in parts:
            if part.startswith("F"):
                try:
                    second_gcode_feed_rates.append(float(part[1:]))
                except ValueError:
                    continue

print("Feed rate extraction completed.")
print("Calculating average feed rates...")

# Calculate the average feed rate for the first G-code file
first_gcode_total_feed_rate = sum(first_gcode_feed_rates)
first_gcode_count = len(first_gcode_feed_rates)
first_gcode_average_feed_rate = first_gcode_total_feed_rate / first_gcode_count if first_gcode_count else 0

# Calculate the average feed rate for the second G-code file
second_gcode_total_feed_rate = sum(second_gcode_feed_rates)
second_gcode_count = len(second_gcode_feed_rates)
second_gcode_average_feed_rate = second_gcode_total_feed_rate / second_gcode_count if second_gcode_count else 0

print("Average feed rate calculation completed.")
print(f"Darco Version Average Feed Rate: {first_gcode_average_feed_rate} mm/min")
print(f"Non-Darco Version Average Feed Rate: {second_gcode_average_feed_rate} mm/min")

# Return the average feed rates for further use
first_gcode_average_feed_rate, second_gcode_average_feed_rate
