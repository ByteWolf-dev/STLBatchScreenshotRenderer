import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
screenshots_folder = os.path.join(script_dir, "STLFiles", "screenshots")

def remove_large_dimension_images(folder):
    pattern = re.compile(r'(\d+)x(\d+)', re.IGNORECASE)
    max_dim = 5

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.png'):
                print(f"Checking file: {file}")  # Debug: show each png file

                match = pattern.search(file)
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    print(f"  Found dimensions: {x}x{y}")

                    if x > max_dim or y > max_dim:
                        file_path = os.path.join(root, file)
                        print(f"  Removing file: {file_path}")
                        os.remove(file_path)
                else:
                    print("  No dimension pattern found in filename.")

if __name__ == "__main__":
    if os.path.isdir(screenshots_folder):
        remove_large_dimension_images(screenshots_folder)
        print("✅ Removal complete.")
    else:
        print(f"Error: screenshots folder not found: {screenshots_folder}")
