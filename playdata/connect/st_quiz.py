# st_quiz.py
import streamlit as st
import sql_test
from db_config import Config
import numpy as np

st.title('[PLAYDATA] SQL QUIZ')

add_selectbox = st.sidebar.selectbox(
    "무엇을 하시고 싶으신가요?",
    ("문제제출", "문제풀기", "나의 성적 확인하기")
)


if add_selectbox =='문제제출':
    st.header('SQL QUIZ 내기')

    input_group=st.text_input("Quiz Group을 입력해주세요 💡 ")


    col1, col2 = st.columns(2)

    with col1:
        input_question=st.text_input(
            "Question :question:"
        )

    with col2:
        input_answer=st.text_input(
            "Answer :heavy_exclamation_mark:"
        )
    
    if st.button('submit'):
        st.write('새로운 문제 제출 감사합니다.')

        sql_test.quiz_insert(input_group,input_question,input_answer)

        with st.container():
            st.write("회원님이 제출하신 문제입니다. 😆")

            st.markdown(f"""## {input_group}""",True)
    
            st.markdown(f"Question : {input_question}")
            st.markdown(f"Answer : {input_answer}")

if add_selectbox =='문제풀기':
    st.write('~~~~~~미완성~~~~~~~')
    # st.write(Sql_quiz(Config).get_quiz_group())
    # tab1, tab2 = st.tabs(Sql_quiz(Config).get_quiz_group())