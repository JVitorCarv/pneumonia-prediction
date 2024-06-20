import threading
from scrapper_ddg import search_and_download_images
from bing_image_downloader import downloader


def ddg_download(
    search_term: str, folder_path: str = ".", max_results: int = 10
) -> None:
    search_and_download_images(search_term, folder_path, max_results)


def bing_download(
    search_term: str,
    limit: int = 10,
    output_dir: str = ".",
    force_replace: bool = False,
    timeout: int = 2,
    verbose: bool = True,
) -> None:
    downloader.download(
        search_term,
        limit=limit,
        output_dir=output_dir,
        force_replace=force_replace,
        timeout=timeout,
        verbose=verbose,
    )


if __name__ == "__main__":
    fiat_search_term = "Fiat Uno Mille"

    thread1 = threading.Thread(
        target=ddg_download, args=(fiat_search_term, "fiat1", 500)
    )
    thread2 = threading.Thread(
        target=bing_download, args=(fiat_search_term, 500, "fiat2", False, 2, True)
    )

    gol_search_term = "VW Gol BX"

    thread3 = threading.Thread(target=ddg_download, args=(gol_search_term, "gol1", 500))
    thread4 = threading.Thread(
        target=bing_download, args=(gol_search_term, 500, "gol2", False, 2, True)
    )

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
