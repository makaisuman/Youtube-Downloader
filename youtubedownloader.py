import streamlit as st

st.title("Nepal Class in 2025")

st.header("Nepal Class in 2025") # primary section
st.subheader("Nepal Class in 2025") # subsection

st.write("Nepal Class in 2025")

st.write("NER identifies and classifies key entities (such as\
people, places, organizations, dates, etc.) within text.\
For example, in the sentence Apple Inc. was founded in 1976, NER would recognize Apple Inc.\
as an organization and 1976 as a date.")

st.button("submit",  type="primary")

st.button("submit",  type="secondary")

st.checkbox("Male", value=True)
st.selectbox("fruits", ["Apple", "Banana", "Cherry"], placeholder="choose a fruit")

#st.write("You can only enter a maximum of 200 characters")
text_var = st.text_input("career summary", value="", max_chars=200, placeholder="You can only enter a maximum of 200 characters")
if len(text_var) != 0:
    st.write("we saw that you wrote this:", text_var)
else:
    print("")


st.number_input("age", min_value=1, max_value=20, placeholder="age between 15 and 60", value=15)
st.slider("year", min_value=2000, max_value=2050, step=2)

data = st.file_uploader("upload file", type=["csv", "txt"])

if data:
    st.write("file uploaded successfully")