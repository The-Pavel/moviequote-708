import streamlit as st

from bbquote.quotes import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

quote