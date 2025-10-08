import logging
from fastapi import FastAPI
from src.routes import router

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
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Redirecter API is running!"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)