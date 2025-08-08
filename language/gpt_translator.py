from openai import OpenAI
import time
import os
from dotenv import load_dotenv


def translate_openai(text, lang_detiny):
    consulta = f"Translate: {text} into {lang_detiny}"
    temperatura = 0.6
    mensajes = [{"role": "system", "content": '''You are a chatbot specialized in translation in multiple languages with a high level of understanding. Example:
                Query: Translate Hello World into English.
                Response: Hello World'''},
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