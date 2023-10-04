# Programmer: Chris Heise (crheise@icloud.com)
# Course: BSSD 4350 - Agile Methodologies
# Instructor: Jonathan Lee
# Program: POC for Second Page of Editor App
# File: launch.py

import gradio as gr
from difflib import Differ

EXAMPLE_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ultricies elementum nulla, id placerat nunc efficitur non. Nam tempus, nulla ac sodales laoreet, lacus tellus efficitur enim, eget sodales lorem ante ut neque. Mauris quis eros sed velit mollis porta. Aenean libero diam, sagittis sed arcu non, fermentum tincidunt leo. Nulla sed velit tempor, dapibus ex in, rhoncus orci. Praesent sit amet odio sagittis arcu venenatis consequat vitae vitae tortor. Sed et maximus nunc, nec placerat ligula.

Etiam libero nisi, fringilla a imperdiet in, luctus a tortor. Pellentesque quis venenatis velit, quis malesuada nisl. Praesent eu placerat ante. Vivamus quis mi porttitor, faucibus purus non, tempus lacus. Pellentesque et imperdiet dui. Vivamus ut lacus quis lacus maximus iaculis. Vivamus mollis odio orci, ut egestas nisl rhoncus nec. Quisque sit amet lorem viverra, lobortis erat quis, consectetur augue. Etiam blandit tempus purus nec maximus. Vestibulum tempus semper ipsum ac faucibus."""

CORRECTED_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ultricies elementum nulla, id placerat nunc efficitur non. Nulla ac sodales laoreet, lacus tellus efficitur enim, eget sodales lorem ante ut neque. Mauris quis eros sed velit mollis porta. Aenean libero diam, sagittis sed arcu non, fermentum tincidunt leo. Nulla sed velit tempor, dapibus ex in, rhoncus orci. Praesent sit amet odio sagittis arcu venenatis consequat vitae vitae tortor. Sed et maximus nunc, nec placerat ligula.

Etiam libero nisi, fringilla a imperdiet in. Pellentesque quis venenatis velit, elit malesuada nisl. Praesent eu placerat ante. Vivamus quis mi porttitor, faucibus purus non, tempus lacus. Pellentesque et imperdiet dui. Vivamus ut lacus quis lacus maximus iaculis. Vivamus mollis odio orci, ut egestas nisl rhoncus nec. Quisque sit amet lorem viverra, lobortis erat quis, consectetur augue. Etiam blandit tempus purus nec maximus. Vestibulum tempus semper ipsum ac tortor."""

def load_text(temp_file):
    temp_file.seek(0)
    return temp_file.read()

def diff_texts(text1, text2):
    d = Differ()
    return [
        (token[2:], token[0] if token[0] != " " else None)
        for token in d.compare(text1, text2)
    ]

with gr.Blocks() as second_page:
    gr.Markdown("Type, Paste, or Upload your text below")
    with gr.Tab("Type/Paste"):
        text_input = gr.Textbox(
            label="Your Text",
            info="Your original text.",
            lines=10,
            value=EXAMPLE_TEXT,
        )
        text_button = gr.Button("Submit")
        corrected_text = gr.Textbox(
            label="Corrected Text",
            info="Our suggested corrected text",
            lines=10,
            value=CORRECTED_TEXT,
            visible=False,
        )
        corrections = gr.HighlightedText(
            label="Corrections",
            combine_adjacent=True,
            show_legend=True,
            color_map={"+": "green", "-": "red"},
        )
        text_button.click(diff_texts, inputs=[text_input, corrected_text], outputs=[corrections])
    with gr.Tab("Upload"):
        file_input = gr.File(
            file_types=["text"],
        )
        loaded_text = gr.Textbox(
            label="Your Text",
            info="The text you uploaded.",
            lines=10,
        )
        file_button = gr.Button("Submit")
        corrected_text = gr.Textbox(
            label="Corrected Text",
            info="Our suggested corrected text",
            lines=10,
            value=CORRECTED_TEXT,
            visible=False,
        )
        corrections = gr.HighlightedText(
            label="Corrections",
            combine_adjacent=True,
            show_legend=True,
            color_map={"+": "green", "-": "red"},
        )
        file_input.upload(load_text, inputs=[], outputs=[loaded_text])
        file_button.click(diff_texts, inputs=[loaded_text, corrected_text], outputs=[corrections])
        # File Input passes the uploaded file as a tempfile._TemporaryFileWrapper
        # TODO: figure out how to open/read the content of the tempfile

second_page.launch()
