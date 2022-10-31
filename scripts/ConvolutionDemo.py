import numpy as np
import gradio as gr


def convolution(img: np.ndarray, *numbers: float):
    
    filter = []
    for number in numbers[:-1]:
        filter.append(number)
        
    step = numbers[-1]
    
    fdim = int(np.sqrt(len(filter)))
    
    height, width, channels= img.shape
    
    newImg = np.zeros((height-fdim+1, width-fdim+1, channels))
    
    print(newImg.shape)   
    for c in range(channels):
        print(f"Channel {c}")
        for x in range(width-fdim+1):
            for y in range(height-fdim+1):
                for i in range(fdim):
                    for j in range(fdim):
                        newImg[y,x,c] += img[y+j,x+i,c]*filter[i+j*fdim]
    
    if -newImg.min() > newImg.max():
        newImg /= newImg.min()
    else:
        newImg /= newImg.max()
    
    return newImg

def main():

    with gr.Blocks() as demo:
        gr.Markdown("# What does a convolutional filter see?")
        
        with gr.Row():
            dim = gr.Number(3, interactive=False, label="Filter dimension")
            dimValue = int(dim.value)
            step = gr.Number(1, interactive=True, label="Filter step")

        filterInputs = []    
        
        with gr.Row():
            with gr.Column():
                image_input = gr.Image()
                for i in range(dimValue):
                    with gr.Row():
                        for j in range(dimValue):
                            filterInputs.append(gr.Number(1))
            image_output = gr.Image()
        
        button = gr.Button("Filter image")
        
        # for number in filterInputs:
        #     number.change(convolution, inputs=[image_input] + filterInputs + [step], outputs=image_output)
        button.click(convolution, inputs=[image_input] + filterInputs + [step], outputs=image_output)
        

    demo.launch()

if __name__ == "__main__":
    main()