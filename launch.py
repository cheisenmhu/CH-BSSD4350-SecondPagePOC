import gradio as gr

with gr.Blocks() as second_page:
    gr.Markdown("Type, Paste, or Upload your text here:")
    with gr.Tab("Type/Paste"):
        text_input = gr.Textbox()
        text_button = gr.Button("Submit")
    with gr.Tab("Upload"):
        file_input = gr.File()
        file_button = gr.Button("Submit")


second_page.launch()
