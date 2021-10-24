from aiohttp import web

from views import index, login, action_login


def setup_routes(app: web.Application) -> None:
    app.add_routes([web.get('/', index)])
    app.add_routes([web.get('/login', login)])
    app.add_routes([web.get('/api/v1/login', action_login)])
