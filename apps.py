import streamlit as st
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import spacy
from spacy.lang.ru.stop_words import STOP_WORDS
# from spacy.lang.el.stop_words import STOP_WORDS
import pandas as pd
import requests
from bs4 import BeautifulSoup
def get_page_text(url):
    html_page = requests.get(url).content
    soup = BeautifulSoup(html_page, 'lxml')
    whitelist = ['h1', 'h2', 'h3','strong','b','u','em','i','ins','p','br','hr']
    out = ""

    for t in soup.find_all(text=True):
        if t.parent.name in whitelist:
            out += '{} '.format(t)

    escape = ['\r', '\n', '\t', '\xa0']
    for e in escape:
        out = out.replace(e, '')
    return out
# nlp = spacy.load('ru_core_news_lg')

desc = "Какое-то описание сайта"

st.title("Fact-Checking News!")
st.markdown(desc)
select_input = st.radio("Выбор:", ["URL", "Текст"])

if select_input == "URL":
    url = st.text_input("URL")
    if st.button("Старт!"):
        # print(url)
        text = get_page_text(url)
        print(text)
        # generate_output(text)

else:
    text = st.text_area("Текст", height=400)
    if st.button("Старт!"):
        print(text)
        # generate_output(text)
