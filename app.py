import gradio as gr

from llm import response

with gr.Blocks() as llm:
    slider = gr.Slider(10, 100, render=False)
    gr.ChatInterface(response, multimodal=True)

llm.launch(debug=True)
