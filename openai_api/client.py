import google.generativeai as genai
from dotenv  import load_dotenv
import os

load_dotenv()

def get_car_ai_bio(model, brand, year):
    
    prompt = "De uma descrição sobre o carro {} {} {} com no máximo 400 caracteres, não precisa citar a brand do carro"

    genai.configure(api_key=os.getenv('secret_key'))
    prompt = prompt.format(brand, model, year)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')

    response = gemini_model.generate_content(prompt)
    return response.text
