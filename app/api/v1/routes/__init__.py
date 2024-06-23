from .voters import router as voters_router
from .elections import router as elections_router
from .legislators import router as legislators_router

__all__ = [voters_router, elections_router, legislators_router]
