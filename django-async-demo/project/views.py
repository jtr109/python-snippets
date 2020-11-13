import asyncio
import random
from typing import List

import aiohttp
from asgiref.sync import async_to_sync
from django.http.response import HttpResponse


async def request_one(url: str) -> str:
    seconds = random.randint(1, 2)
    print(f'request {url}')
    # asyncio 中不能使用 requests 模块，由于 requests 模块是同步的，请求还是会同步执行。
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'get response from {url}')
    return url


@async_to_sync
async def request_all(urls: List[str]):
    results = await asyncio.gather(
        *[request_one(u) for u in urls]
    )
    print(results)


def run(urls: List[str]):
    # async_to_sync 的转换可以放在调用栈的任何深度
    request_all(urls)


# https://docs.djangoproject.com/en/3.1/topics/async/
def hello(request):
    urls = [
        'https://www.github.com',
        'https://www.baidu.com',
        'https://www.zhihu.com',
        'https://www.godaddy.com',
    ]
    run(urls)
    return HttpResponse('hello')
