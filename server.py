from fastapi import FastAPI, Form, HTTPException
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

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    return {'locations': locations}

# ////////////
# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
# //////////
@app.post('/predict_home_price')
async def predict_home_price(total_sqft: float = Form(...), location: str = Form(...), bhk: int = Form(...), bath: int = Form(...)):
    try:
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'estimated_price': estimated_price}

if __name__ == "__main__":
    print("Starting Python FastApi Server For Home Price Prediction...")
    util.load_saved_artifacts()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
