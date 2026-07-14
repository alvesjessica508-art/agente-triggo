import gradio as gr
from agent import responder


def chat(message, history):
    return responder(message)


demo = gr.ChatInterface(
    chat,
    title="Agente Triggo AI",
    description="Agente desenvolvido com Gemini 3.1 Flash Lite"
)


demo.launch()