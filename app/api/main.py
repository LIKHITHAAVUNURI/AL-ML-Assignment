app/api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model_loader import find_best_recipe

app = FastAPI()

class IngredientInput(BaseModel):
    ingredients: list

@app.post("/get-recipe")
def get_recipe(data: IngredientInput):
    result = find_best_recipe(data.ingredients)
    return {
        "input": data.ingredients,
        "suggested_recipe": result["recipe"],
        "similarity_score": result["score"]
    }
