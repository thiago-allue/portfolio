import asyncio

import aiohttp
import aiofiles
import async_timeout


async def download_file(filename, url, session):
    async with async_timeout.timeout(120):
        async with session.get(url) as response:
            with aiofiles.open(filename, 'wb') as fd:
                async for data in response.content.iter_chunked(1024):
                    fd.write(data)
        return 'Successfully downloaded ' + filename


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(filename, url, session) for filename, url in urls]
        return await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = [("filename.zip", "http://url/filename.zip")]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main(urls))
    print(results)
