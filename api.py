from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
import uvicorn


app = Starlette()


@app.route('/')
class PingResource(HTTPEndpoint):

    async def get(self, request):
        return JSONResponse(dict(ping="Pong yo."))
