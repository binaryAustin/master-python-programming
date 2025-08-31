import asyncio
import aiohttp
import aiofiles


async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        html = await res.text()
        return html


async def write_to_file(file, text):
    async with aiofiles.open(file, mode="w") as f:
        await f.write(text)


async def main(urls_param):
    tasks = []
    for url in urls_param:
        file = f"{url.split('//')[-1]}.txt"
        html = await fetch(url)
        tasks.append(write_to_file(file, html))

    await asyncio.gather(*tasks)


urls = ("https://python.org", "https://stackoverflow.com", "https://google.com")
asyncio.run(main(urls))
