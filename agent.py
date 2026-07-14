from google import genai

from config import API_KEY, MODEL
from prompts import SYSTEM_PROMPT

client = genai.Client(api_key=API_KEY)


def responder(pergunta):

    prompt = f"""
{SYSTEM_PROMPT}

Usuário:
{pergunta}
"""

    resposta = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return resposta.text