import os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from utils.files import clear_data_directory


def resize_and_crop_image(
    input_file: str, output_file: str, target_size: int = 256, crop_size: int = 224
) -> None:
    """
    Resize an image to the target size and then crop the center to the crop size.

    Args:
        input_file (str): Path to the input image file.
        output_file (str): Path to the output image file.
        target_size (int): Size to resize the image to (default is 256x256).
        crop_size (int): Size to crop the center of the image (default is 224x224).
    """
    with Image.open(input_file) as img:
        img = img.resize((target_size, target_size), Image.LANCZOS)

        left = (target_size - crop_size) / 2
        top = (target_size - crop_size) / 2
        right = (target_size + crop_size) / 2
        bottom = (target_size + crop_size) / 2

        img = img.crop((left, top, right, bottom))

        img.save(output_file, "JPEG")


def process_image_file(input_file: str, output_file: str) -> None:
    resize_and_crop_image(input_file, output_file)
    print(f"Processed {input_file} to {output_file}")


def process_image_directory(
    input_dir: str, output_dir: str, max_workers: int = 12
) -> None:
    """
    Process all image files in a directory, resize and crop them, and save them to the output directory.

    Args:
        input_dir (str): Path to the directory containing image files.
        output_dir (str): Path to the directory to save processed image files.
        max_workers (int): Maximum number of threads to use.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith((".jpeg", ".jpg", ".png")):
                    input_file = os.path.join(root, file)
                    output_file = os.path.join(
                        output_dir, os.path.splitext(file)[0] + ".jpeg"
                    )
                    futures.append(
                        executor.submit(process_image_file, input_file, output_file)
                    )

        for future in futures:
            future.result()


def main() -> None:
    directories = {
        "./data/raw_dataset/train/normal": "./data/resized/train/normal",
        "./data/raw_dataset/train/pneumonia": "./data/resized/train/pneumonia",
        "./data/raw_dataset/test/normal": "./data/resized/test/normal",
        "./data/raw_dataset/test/pneumonia": "./data/resized/test/pneumonia",
    }

    for input_dir, output_dir in directories.items():
        process_image_directory(input_dir, output_dir)

    clear_data_directory("./data", keep="resized")


if __name__ == "__main__":
    main()
