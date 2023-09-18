import os
from aiohttp import web
root = os.environ.get('SCRIPT_NAME', '/apps/app123')

app = web.Application()


@web.middleware
async def add_trailing(request, handler):
    if not request.path.endswith('/'):
        new_path = request.path + '/'
        return web.HTTPMovedPermanently(new_path)
    else:
        return await handler(request)


async def hello(request):
    return web.Response(text="This is a Custom App")

app.add_routes([web.get(f'{root}/', hello)])
app.middlewares.append(add_trailing)
web.run_app(app)
