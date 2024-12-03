from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserLogin(BaseModel):
    name: str
    room: str | None = None
    roomPwd: str | None = None

@router.post("/login")
async def loginuser(user_login: UserLogin):
    """
    define a mongodb schema that looks like this:
    class RoomInfo():
        room: str
        roomPwd: str
        members: {
            member1: name1
        }
        roomValid: bool
    """
    return "login success"