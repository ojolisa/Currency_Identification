import pathlib
import textwrap
import streamlit as st
from PIL import Image

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


st.title('Currency description')

genai.configure(api_key=st.secrets["api_key"])
model = genai.GenerativeModel('gemini-pro-vision')

uploaded_file = st.file_uploader(
    "Upload a currency note or coin.", type=["jpg", "png", "jpeg"])

if st.button("Ask"):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)

        response = model.generate_content(["Give a discription of the currency present in the image. It's country of use, name, denomination etc. If the image does not have a currency, refuse to answer",img])
        st.write(to_markdown(response.text).data)
    else:
        st.write("Please upload an image of the currency first")    
