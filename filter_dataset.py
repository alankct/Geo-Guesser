"""
filter_dataset.py is a program I created to filter our Geoguessr dataset.

This is made for unevenly distributed data, set the global variables and you can:
    1. Delete random files from any sub-folder until you reach MAX_IMGS_PER_COUNTRY
    2. Delete sub-folders with less than COUNTRY_MIN_IMGS
"""

import os
import random
import shutil

# Set the maximum number of images (files) for each country (sub-folder)
MAX_IMGS_PER_COUNTRY = 1000
# Set the minimum number of images per country. If a country does not pass this limit, it is deleted
COUNTRY_MIN_IMGS = 50

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def remove_files_randomly(folder_path, max_images):
    folder_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Continue removing files until the number of images is reduced to max_images
    while len(folder_files) > max_images:
        file_to_remove = random.choice(folder_files)
        file_to_remove_path = os.path.join(folder_path, file_to_remove)
        os.remove(file_to_remove_path)
        folder_files.remove(file_to_remove)
        # print(f"Removed file: {file_to_remove}")

if __name__ == "__main__":
    
    root_folder = "Users/user/example/dataset/path"

    max_images_per_country = MAX_IMGS_PER_COUNTRY
    min_images_to_delete = COUNTRY_MIN_IMGS

    # Loop through subfolders (countries) in the root folder
    for country_folder in os.listdir(root_folder):
        country_path = os.path.join(root_folder, country_folder)

        if os.path.isdir(country_path):
            # num_images = len([f for f in os.listdir(country_path) if os.path.isfile(os.path.join(country_path, f))])
            num_images = get_folder_size(country_path)

            if num_images > max_images_per_country:
                print(f"Reducing images from {country_folder} folder...")
                remove_files_randomly(country_path, max_images_per_country)
            elif num_images < min_images_to_delete:
                print(f"Deleting {country_folder} folder with {num_images} images...")
                shutil.rmtree(country_path)