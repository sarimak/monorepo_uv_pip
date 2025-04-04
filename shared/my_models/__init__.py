import pydantic


class MyMessage(pydantic.BaseModel):
    name: str
