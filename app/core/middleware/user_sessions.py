import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import json
from app.core.redis import RedisPool


class RedisSessionMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: FastAPI,
        redis_pool: RedisPool,
        session_cookie: str = "session_id",
        max_age: int = 3600,
    ):
        super().__init__(app)
        self.redis_pool = redis_pool
        self.session_cookie = session_cookie
        self.max_age = max_age

    async def dispatch(self, request: Request, call_next):
        session_id = request.cookies.get(self.session_cookie)
        if not session_id:
            # No session cookie found, create a new session
            session_id = str(uuid.uuid4())
            session_data = {}
        else:
            # Retrieve session data from Redis
            session_data = await self.redis_pool.get(session_id)
            if session_data:
                session_data = json.loads(session_data)
            else:
                session_data = {}

        # Attach session data to the request state
        request.state.session = session_data

        # Process the request
        response = await call_next(request)

        # After the response, store the session data back to Redis
        session_data = request.state.session
        await self.redis_pool.set(
            session_id, json.dumps(session_data), expire=self.max_age
        )

        # Set the session cookie in the response
        response.set_cookie(
            key=self.session_cookie,
            value=session_id,
            max_age=self.max_age,
            httponly=True,
            secure=True,  # Ensure this is set to True in production
            samesite="Lax",
        )

        return response
