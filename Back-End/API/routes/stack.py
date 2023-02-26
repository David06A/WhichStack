from fastapi import APIRouter

router = APIRouter(
    prefix="/stack",
)


@router.get("/getinfo")
async def get_info():
    return 200
    