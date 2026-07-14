from agent import responder

print("=" * 40)
print("Agente Triggo")
print("=" * 40)

while True:

    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        break

    resposta = responder(pergunta)

    print("\nAgente:", resposta)