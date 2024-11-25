from typing import Annotated

from fastapi import APIRouter, Form

from auth import LoginFormData

api = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@api.post("/login")
async def login(form: Annotated[LoginFormData, Form()]):
    return form
