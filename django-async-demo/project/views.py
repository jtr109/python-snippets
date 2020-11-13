import asyncio
import random
from typing import List

from asgiref.sync import async_to_sync
from django.http.response import HttpResponse


async def request_one(url: str) -> str:
    seconds = random.randint(1, 2)
    print(f'request {url}')
    await asyncio.sleep(seconds)  # request a url
    print(f'get response from {url}')
    return ''.join(list(reversed(url)))


@async_to_sync
async def request_all(urls: List[str]):
    results = await asyncio.gather(
        *[request_one(u) for u in urls]
    )
    print(results)


# https://docs.djangoproject.com/en/3.1/topics/async/
def hello(request):
    request_all(urls=['foo', 'bar'])
    return HttpResponse('hello')
