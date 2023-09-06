# # import gradio as gr
# # from modules import scripts

# # class NewUIScript(scripts.Script):

# #     def title(self):
# #         return "NewUI"

# #     def ui(self, is_img2img):
# #         with gr.Group():
# #             with gr.Accordion("Send centrum", open=False):
# #                 send_text_button = gr.Button(value='send text', variant='primary')
# #                 text_to_be_sent = gr.Textbox(label="drop text")

# #         with contextlib.suppress(AttributeError):  # Ignore the error if the attribute is not present
# #             if is_img2img:
# #                 # Bind the click event of the button to the send_text_to_prompt function
# #                 # Inputs: text_to_be_sent (textbox), self.boxxIMG (textbox)
# #                 # Outputs: self.boxxIMG (textbox)
# #                 send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxxIMG], outputs=[self.boxxIMG])
# #             else:
# #                 # Bind the click event of the button to the send_text_to_prompt function
# #                 # Inputs: text_to_be_sent (textbox), self.boxx (textbox)
# #                 # Outputs: self.boxx (textbox)
# #                 send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxx], outputs=[self.boxx])

# #         return [text_to_be_sent, send_text_button]


# #     def after_component(self, component, **kwargs):
# #         prefix = "txt2img" if self.is_txt2img else "img2img"

# #         # if kwargs.get("elem_id") == f"{prefix}_toprow":
# #         #     gr.Button('custom button')

import contextlib

import gradio as gr
from modules import scripts
from modules import script_callbacks

class NewUIScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "NewUI"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return 

    def process(self, p):
        neg_prompts = ["ugly, deformed, noisy, blurry, low contrast, distorted, grainy"]
        for i, prompt in enumerate(neg_prompts):
                p.all_negative_prompts[i] = prompt
                
    def after_component(self, component, **kwargs):
        return component









