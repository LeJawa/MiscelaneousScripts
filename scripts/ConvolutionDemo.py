import numpy as np
import gradio as gr


def convolution(img, *numbers):
    return img

with gr.Blocks() as demo:
    gr.Markdown("# What does a convolutional filter see?")
    dim = gr.Number(3, interactive=False, label="Filter dimension")

    filterInputs = []    
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image()
            for i in range(int(dim.value)):
                with gr.Row():
                    for j in range(int(dim.value)):
                        filterInputs.append(gr.Number())
        image_output = gr.Image()
    
    
    for number in filterInputs:
        number.change(convolution, inputs=[image_input] + filterInputs, outputs=image_output)
    

demo.launch()