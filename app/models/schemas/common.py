from fastapi.responses import ORJSONResponse

from typing import Generic, Optional, TypeVar, Optional

T = TypeVar("T")

class V1HttpResponse(ORJSONResponse):
    def __init__(self, content: Optional[T] = None, **kwargs):
        super().__init__(
            content={
                "message": "OK",
                "statusCode": "BM20000",
                "data": content,
            },
            **kwargs
        )