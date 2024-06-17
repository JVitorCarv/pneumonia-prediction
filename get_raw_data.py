import os
from dcm_converter import process_directory
from file_utils import move_files, move_random_files, process_csv, sort_and_rename_files

RSNA_PATH = "rsna-pneumonia-detection-challenge"
CHEST_XRAY_PATH = "archive/chest_xray"
RAW_PATH = "raw_dataset"
SEED = 913


def process_data():
    print("Processing training data...")
    process_directory(
        f"{RSNA_PATH}/stage_2_train_images", f"{RSNA_PATH}/train", max_workers=12
    )
    print("Processing test data...")
    process_directory(
        f"{RSNA_PATH}/stage_2_test_images", f"{RSNA_PATH}/test", max_workers=12
    )


def process_labels():
    process_csv(
        f"{RSNA_PATH}/stage_2_train_labels.csv",
        f"{RSNA_PATH}/train",
        f"{RSNA_PATH}/renamed",
        max_workers=12,
    )


def organize_directories():
    directories = [
        f"{CHEST_XRAY_PATH}/train/NORMAL",
        f"{CHEST_XRAY_PATH}/train/PNEUMONIA",
        f"{CHEST_XRAY_PATH}/test/NORMAL",
        f"{CHEST_XRAY_PATH}/test/PNEUMONIA",
        f"{RSNA_PATH}/renamed/normal",
        f"{RSNA_PATH}/renamed/pneumonia",
    ]

    for directory in directories:
        if os.path.exists(directory):
            print(f"Organizing directory: {directory}")
            sort_and_rename_files(directory)
        else:
            print(f"Directory {directory} does not exist")


def move_validation_files():
    move_files(f"{CHEST_XRAY_PATH}/val/NORMAL", f"{CHEST_XRAY_PATH}/test/NORMAL")
    move_files(f"{CHEST_XRAY_PATH}/val/PNEUMONIA", f"{CHEST_XRAY_PATH}/test/PNEUMONIA")


def move_random_samples():
    move_random_files(
        f"{CHEST_XRAY_PATH}/train/NORMAL", f"{CHEST_XRAY_PATH}/test/NORMAL", 41, SEED
    )
    move_random_files(
        f"{CHEST_XRAY_PATH}/train/PNEUMONIA",
        f"{CHEST_XRAY_PATH}/test/PNEUMONIA",
        42,
        SEED,
    )


def move_files_to_raw_dataset():
    train_path = f"{RAW_PATH}/train"
    test_path = f"{RAW_PATH}/test"

    # Move XRAY files
    move_files(
        f"{CHEST_XRAY_PATH}/train/NORMAL", f"{train_path}/normal", dest_prefix="xray_"
    )
    move_files(
        f"{CHEST_XRAY_PATH}/test/NORMAL", f"{test_path}/normal", dest_prefix="xray_"
    )
    move_files(
        f"{CHEST_XRAY_PATH}/test/PNEUMONIA",
        f"{test_path}/pneumonia",
        dest_prefix="xray_",
    )
    move_random_files(
        f"{CHEST_XRAY_PATH}/train/PNEUMONIA",
        f"{train_path}/pneumonia",
        2000,
        SEED,
        dest_prefix="xray_",
    )

    # Move RSNA files
    rsna_normal_path = f"{RSNA_PATH}/renamed/normal"
    rsna_pneumonia_path = f"{RSNA_PATH}/renamed/pneumonia"

    move_random_files(
        rsna_normal_path, f"{train_path}/normal", 1700, SEED, dest_prefix="rsna_"
    )
    move_random_files(
        rsna_normal_path, f"{test_path}/normal", 375, SEED, dest_prefix="rsna_"
    )
    move_random_files(
        rsna_pneumonia_path, f"{train_path}/pneumonia", 2000, SEED, dest_prefix="rsna_"
    )
    move_random_files(
        rsna_pneumonia_path, f"{test_path}/pneumonia", 440, SEED, dest_prefix="rsna_"
    )


def main():
    process_data()
    process_labels()
    move_validation_files()
    move_random_samples()
    organize_directories()
    move_files_to_raw_dataset()


if __name__ == "__main__":
    main()
