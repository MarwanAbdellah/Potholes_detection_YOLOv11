from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from medium_inference import medium_inference
from large_inference import large_inference
from PIL import Image
import io

app = FastAPI()

@app.post("/predict_medium/")
async def predict_medium(file: UploadFile = File(...)):

    image = Image.open(file.file)

    result = medium_inference(image)
    
    buffer = io.BytesIO()   # Create a buffer to hold the image data

    result.save(buffer, format="JPEG")  # Save the result image to the buffer
    buffer.seek(0) # Reset buffer position to the beginning
    return StreamingResponse(buffer, media_type="image/jpeg")

@app.post("/predict_large/")
async def predict_large(file: UploadFile = File(...)):

    image = Image.open(file.file)

    result = large_inference(image)
    
    buffer = io.BytesIO()

    result.save(buffer, format="JPEG")  
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/jpeg")
