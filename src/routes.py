import logging

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/qr")
LOGGER = logging.getLogger(__name__)


@router.get("/redirect/mata")
async def redirect_mata_channel():
    """Endpoint to redirect to the Mata channel."""
    return RedirectResponse(url="https://whatsapp.com/channel/0029VbB2ccoIHph8k7yfT01H")