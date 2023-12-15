import os
import random
import shutil

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def remove_files_randomly(folder_path, max_images):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Continue removing files until the number of images is reduced to max_images
    while len(files) > max_images:
        file_to_remove = random.choice(files)
        file_path = os.path.join(folder_path, file_to_remove)
        os.remove(file_path)
        print(f"Removed file: {file_to_remove}")
        files.remove(file_to_remove)

def delete_subfolders_less_than(folder_path, min_images):
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)

        # Check if it's a directory
        if os.path.isdir(subfolder_path):
            # Get the number of images in the subfolder
            num_images = len([f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))])

            # If the subfolder has fewer than min_images, delete it
            if num_images < min_images:
                print(f"Deleting subfolder {subfolder} with {num_images} images...")
                shutil.rmtree(subfolder_path)

if __name__ == "__main__":
    
    root_folder = "/Users/acasey/Downloads/50k_geoguessr_BALANCED/"

    # Set the maximum number of images for each country
    max_images_per_country = 1000
    # Set the minimum number of images for subfolders to be deleted
    min_images_to_delete = 50

    # Loop through subfolders (countries) in the root folder
    for country_folder in os.listdir(root_folder):
        country_path = os.path.join(root_folder, country_folder)

        # Check if it's a directory
        if os.path.isdir(country_path):
            # Get the number of images in the country folder
            num_images = len([f for f in os.listdir(country_path) if os.path.isfile(os.path.join(country_path, f))])

            # If the country folder has more than max_images_per_country images, remove random files
            if num_images > max_images_per_country:
                print(f"Processing {country_folder} folder...")
                remove_files_randomly(country_path, max_images_per_country)
            # If the country folder has fewer than min_images_to_delete, delete the entire folder
            elif num_images < min_images_to_delete:
                print(f"Deleting {country_folder} folder with {num_images} images...")
                shutil.rmtree(country_path)