import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

HtmlFile = open("bootstraptest.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code,height=1200)
