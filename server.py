from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()
# Configurer les origines autorisées pour CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou spécifie les origines autorisées spécifiques
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.get('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    return {'locations': locations}

if __name__ == "__main__":
    print("Starting Python FastApi Server For Home Price Prediction...")
    util.load_saved_artifacts()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
