from flask import Flask # type: ignore
from flask_limiter import Limiter # type: ignore
from fastapi import FastAPI # type: ignore
from fastapi.openapi.utils import get_openapi # type: ignore
from slowapi import Limiter # type: ignore
from slowapi.util import get_remote_address # type: ignore
from fastapi.middleware.trustedhost import TrustedHostMiddleware # type: ignore

app = FastAPI()
# define openapi metadata
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My API",
        version="1.0.0",
        description="This is a description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app = Flask(__name__)

##limiter
limiter = Limiter(get_remote_address, app = app, default_limits=["10 per min"]
)
## setup limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

# apply rate limits globally or to specific routes

@app.get('/resource')
@limiter.limit("5/minute") # allow 5 requests per min
async def resource():
    return {"message": "This resource is rate-limited!"}

