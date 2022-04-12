import os
import sys
import argparse
import datetime
import requests


def log(msg):
    print(
        '[{}] {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f'), msg)
    )


def download(url):
    try:
        os.makedirs('downloads')
    except Exception as e:
        log(e)

    try:
        local_filename = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open(os.path.join('downloads', local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        log(e)


def download_list(filename):
    try:
        with open(filename, 'r') as f:
            for url in f:
                download(url)
    except Exception as e:
        log(e)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filename', help='Filename containing one url per line', type=str
    )
    parser.add_argument('-u', '--url', help='Link of file to download', type=str)
    args = parser.parse_args()

    if len(sys.argv) < 1:
        parser.print_help()
        sys.exit(0)

    if args.url:
        download(args.url)

    if args.filename:
        download_list(args.filename)
