import streamlit as st
from transpiler_controller import TranspilerController

controller = TranspilerController()

st.set_page_config(page_title='Transpiler Dart ⬌ Kotlin', layout="wide")
st.title('Transpiler Dart ⬌ Kotlin')
col1, col2 = st.columns(2)

with col1:
    input_code = st.text_area("Write the code you want to convert here", height=300)
    
    source_options = ['dart', 'kotlin']
    target_options = ['dart', 'kotlin']

    source_lang = None
    target_lang = None

    sub_col_1, sub_col_2 = st.columns(2)

    with sub_col_1:
        source_lang = st.selectbox('Select the source language', source_options)
    
    with sub_col_2:
        target_lang = st.selectbox('Select the target language', target_options)

    if st.button('Start Conversion'):
        (output_code, errors) = controller.transpile(input_code, source_lang, target_lang)
        if (errors == None):
            with col2:
                st.text_area('Output', height=300, value=output_code)
        else:
            with col2:
                st.text_area("Oops, something went wrong!", height=300, value=errors)

















