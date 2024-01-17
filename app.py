from fastapi import FastAPI
import pickle

model = pickle.load(open('model.pkl','rb'))

app = FastAPI()

@app.get ("/")
async def predict():
    prediction = model.get_forecast(steps=12).predicted_mean
    return(prediction)