from bing_image_downloader import downloader

if __name__ == "__main__":
    downloader.download(
        "Ahri hentai",
        limit=100,
        output_dir="ahri",
        force_replace=False,
        timeout=2,
        verbose=True,
    )
