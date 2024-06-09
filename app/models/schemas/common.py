from fastapi.responses import ORJSONResponse

from pydantic import BaseModel
from typing import Generic, Optional, TypeVar, Optional

T = TypeVar("T")

class BaseHttpResponse(BaseModel, Generic[T]):
    message: str = "OK"
    statusCode: str = "20000"
    data: Optional[T] = None

class V1HttpResponse(ORJSONResponse):
    def __init__(self, content: Optional[T] = None, **kwargs):
        super().__init__(
            content={
                "message": "OK",
                "statusCode": "20000",
                "data": content,
            },
            **kwargs
        )