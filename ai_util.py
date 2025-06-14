import google.generativeai as genai

def ai_parser(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("pick-your-model")
    response = model.generate_content(prompt)
    return response.text
