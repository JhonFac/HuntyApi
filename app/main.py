import models
from config import engine
from fastapi import FastAPI
from routes import router
from schemas import Response

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def index():
    return Response(status="Ok", code="200", message="Prueba con la url ").dict(exclude_none=True)


app.include_router(router, prefix="/api", tags=["api"])
# app.include_router(router, prefix="/usuarios", tags=["usuarios"])
# app.include_router(router, prefix="/empresas", tags=["empresas"])
# app.include_router(router, prefix="/vacantes", tags=["vacantes"])
