# Feed Rate Comparison Tool

This Python script compares the feed rates between two G-code files, helping to identify any differences in printing performance due to software updates. This tool was developed to verify if a recent software update at my workplace impacted the feeding rate during 3D printing operations, as the new update appeared to cause printing issues.

## Features

- **File Comparison**: Compares two G-code files and identifies the differences.
- **Keyword Filtering**: Focuses on differences related to specific G-code commands for extrusion and purging.
- **Feed Rate Calculation**: Extracts and calculates the average feed rates from the G-code commands in both files.
- **Output**: Provides the average feed rates for both G-code files, allowing for an easy comparison of the software update's impact.

## Prerequisites

- Python 3.x

## Usage

1. Place your two G-code files in the same directory as the script.
2. Replace `'insert your file name'` and `'insert your file name here'` with the filenames of your G-code files in the script.
3. Run the script using the following command:

   ```bash
   python feedrate_calculator.py
