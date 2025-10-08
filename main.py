import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Redirecter API",
    description="A minimal FastAPI project for URL redirection",
    version="1.0.0"
)

# Include routers
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Redirecter API is running!"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}




@app.get("/mata")
async def redirect_mata_channel():
    """Endpoint to redirect to the Mata channel."""
    return RedirectResponse(url="https://whatsapp.com/channel/0029VbB2ccoIHph8k7yfT01H")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)