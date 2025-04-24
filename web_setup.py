import asyncio
import uvloop

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from settings import config_parameters, is_prod
from starlette.middleware.cors import CORSMiddleware

from api.router_global import router


def create_app() -> FastAPI:
    docs_url = '/docs' if not config_parameters.IS_PROD else None
    redoc_url = '/redoc' if not config_parameters.IS_PROD else None
    app = FastAPI(title='Acmenra.CRM', debug=not config_parameters.IS_PROD,
                  docs_url=docs_url, redoc_url=redoc_url,
                  root_path='/api')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(SessionMiddleware, secret_key=config_parameters.SECRET_KEY)

    return app

uvloop.install()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
server = create_app()

server.include_router(router)

if is_prod:
    print('PROD')
