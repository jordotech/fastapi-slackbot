from fastapi import APIRouter

router = APIRouter()


@router.get("/version", name="display_version")
def app_version():
    from main import app

    return {
        "version": app.app.version,
    }
