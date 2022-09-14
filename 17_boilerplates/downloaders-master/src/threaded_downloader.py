import os
import datetime

from concurrent.futures import ThreadPoolExecutor

import requests


def log(msg):
    print(
        "[{}] {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f"), msg)
    )


def download(d):
    filename, url = d
    try:
        os.makedirs("files")
    except Exception as e:
        pass

    try:
        r = requests.get(url, stream=True)
        with open(os.path.join("files", filename), "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if not chunk:
                    break
                f.write(chunk)
        log(f"{filename} downloaded.")
    except Exception as e:
        log(e)


def main():
    urls = [line.strip().split() for line in open("urls.txt", "r") if len(line) > 10]
    with ThreadPoolExecutor() as pool:
        results = pool.map(download, urls)
    list(results)
    log("Done.")


if __name__ == "__main__":
    main()
