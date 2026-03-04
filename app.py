from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.calc import router as calc_router


def create_app() -> FastAPI:
    app = FastAPI(title="Refrigerant Ratio Calculator API", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(calc_router)
    return app


app = create_app()
