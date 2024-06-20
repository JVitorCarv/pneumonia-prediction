from utils.files import move_files, delete_directory
from utils.images import (
    find_and_remove_duplicates,
    remove_corrupted_images,
    filter_dataset,
)

if __name__ == "__main__":
    # move_files("./gol2/VW Gol BX", "./gol")
    # move_files("./gol1", "./gol")
    # move_files("./fiat2/Fiat Uno Mille", "./fiat")
    # move_files("./fiat1", "./fiat")
    # delete_directory("./fiat1")
    # delete_directory("./fiat2")
    # delete_directory("./gol1")
    # delete_directory("./gol2")
    # find_and_remove_duplicates("./fiat")
    # find_and_remove_duplicates("./gol")
    # remove_corrupted_images("./fiat")
    # remove_corrupted_images("./gol")
    # filtered_output_directory = "./filtered_fiat"
    # filter_dataset(
    #     "./fiat", "./fiat_hashes_to_filter.txt", filtered_output_directory
    # )
    # filtered_output_directory = "./filtered_gol"
    # filter_dataset("./gol", "./gol_hashes_to_filter.txt", filtered_output_directory)
    delete_directory("./gol")
    delete_directory("./fiat")
