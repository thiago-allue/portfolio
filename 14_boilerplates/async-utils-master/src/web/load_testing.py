import asyncio
import concurrent.futures

import aiohttp


async def fetch(url, session):
    async with session.get(url, ssl=False) as response:
        j = await response.json()
        print(f'Processed {url}')
        return {url: j}


async def load_test(url='http://localhost:8080', limit=1000):
    async with aiohttp.ClientSession() as session:
        async with asyncio.Semaphore(limit):
            tasks = [fetch(url + f'/{i}', session) for i in range(4)]
            return await asyncio.gather(*tasks)


def main():
    return asyncio.run(load_test())


def process_pool():
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(main): p for p in range(4)}

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
        except Exception as e:
            print(e)
        else:
            print(url, data)


if __name__ == '__main__':
    process_pool()
