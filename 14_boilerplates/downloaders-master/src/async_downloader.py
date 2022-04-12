import pathlib
import asyncio
import aiohttp
import aiofiles


async def download_files(filename, url, session):
    sem = asyncio.Semaphore(8)
    chunk_size = 4 * 1024
    async with sem:
        async with session.get(url) as resp:
            async with aiofiles.open(
                pathlib.Path(__file__).parent.joinpath("files", filename), "wb"
            ) as f:
                while 1:
                    chunk = await resp.content.read(chunk_size)
                    if not chunk:
                        break
                    await f.write(chunk)
            print(f"{filename} downloaded.")


# async def fetch(filename, url):
#     async with aiohttp.ClientSession() as session:
#         await download_files(filename, url, session)


async def process():
    urls = [line.strip().split() for line in open("urls.txt", "r") if len(line) > 10]

    tasks = []
    async with aiohttp.ClientSession() as session:
        for filename, url in urls:
            tasks.append(
                asyncio.wait_for(download_files(filename, url, session), timeout=None)
            )

        await asyncio.gather(*tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process())


if __name__ == "__main__":
    main()
