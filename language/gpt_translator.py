from openai import OpenAI
import time
import os
from dotenv import load_dotenv

#Conexion con Chat GPT para traducir el texto
def translate_openai(text, lang_detiny):
    consulta = f"Translate: {text} into {lang_detiny}"
    temperatura = 0.6
    mensajes = [{"role": "system", "content": '''You are a professional translator who is fluent in several languages and who translates what is requested directly into the desired language without saying anything other than what is requested. You do not ask for context, you do not explain anything, you just translate what is requested as is, Also, you should keep spaces, line breaks, and signs where they are, no matter what, even if there are too many or not enough. 
                Example 1:
                Query: Translate Hello World into English.
                Response: Hello World.
                Example 2:
                Query: Banana extraterrestre montando un caballo cohete.
                Response: Alien banana riding a rocket horse.
                Example 3:
                Query: Pedro tiene hambre.
                Response: Aピーターはお腹が空いています.
                Example 4:
                Query: Banana extraterrestre montando un caballo cohete.
                Response: Alien banana riding a rocket horse.
                Example 5:
                Query: Además, debes mantener      los espacios,      saltos de línea y señales               donde están, sin importar nada,     
                 incluso si son demasiados o no.
                Response: Also, you should      keep spaces,      line breaks and signs               where they are, no matter what,     
                 even if there are too many or not enough.'''},
            {"role": "user", "content": consulta} ]
    try:
        load_dotenv(dotenv_path=".env")
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        resultado = client.chat.completions.create(
            model="gpt-4o-mini",
          messages=mensajes,temperature=temperatura)

    except Exception as e :
        time.sleep(5)
        print(f"Error de conexión: {e}")
        return None
    return resultado.choices[0].message.content