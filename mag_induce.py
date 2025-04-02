import streamlit as st
import json
import numpy as np

# Load the question data from the JSON file
with open("data/qs_3.5.json", "r") as f:
    questions = json.load(f)

st.title("PHY 132 – Activity 3.5 - Magnetic Induction")
st.write("This tool checks your final numerical answers (within 1% tolerance). Enter only the number(s) — no units.")

# Dropdown to select a question
question_ids = list(questions.keys())
selected_id = st.selectbox("Choose a question:", question_ids)

# Retrieve the selected question
q = questions[selected_id]
st.markdown(f"**{q['text']}**")

# Check if the answer is a single number or a list (multiple parts)
if isinstance(q['answer'], list):
    # For multiple answers, create a separate input for each part.
    user_answers = []
    num_parts = len(q['answer'])
    for i in range(num_parts):
        user_input = st.number_input(f"Enter answer part {i+1} in {q['unit']}:", format="%.6f", key=f"{selected_id}_{i}")
        user_answers.append(user_input)
    if st.button("Check Answer"):
        all_correct = True
        for user_ans, correct_ans in zip(user_answers, q['answer']):
            tolerance = 0.01 * abs(correct_ans)
            if abs(user_ans - correct_ans) > tolerance:
                all_correct = False
                break
        if all_correct:
            st.success("✅ Correct! Your answer is within 1% of the expected value.")
        else:
            st.error("❌ Not quite. Try again.")
else:
    # Single numerical answer
    user_answer = st.number_input(f"Enter your answer in {q['unit']}:", format="%.6f")
    if st.button("Check Answer"):
        correct = float(q['answer'])
        tolerance = 0.01 * abs(correct)
        if abs(user_answer - correct) <= tolerance:
            st.success("✅ Correct! Your answer is within 1% of the expected value.")
        else:
            st.error("❌ Not quite. Try again.")

# Footer with contact info and EKU logo
footer = '''
---
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
        This tool was developed for <b>PHY 132 - College Physics II</b> at Eastern Kentucky University.<br>
        For questions, contact: <b>Professor Zakeri</b> (m.zakeri@eku.edu)
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/ZAKI1905/phy132-kirchhoff-checker/main/img/PrimaryLogo_Maroon.png" width="150">
    </div>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)
