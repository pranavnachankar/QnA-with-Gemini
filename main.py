# importing libraries
import streamlit as st
import google.generativeai as genai

# credential
GOOGLE_API_KEY = "YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# function to load gemini pro model to get responses
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(prompt):
	response = model.generate_content(prompt)
	return response.text


# initialize streamlit app
st.set_page_config(page_title="Q&A with Gemini", page_icon="🤖")
st.header("Gemini LLM Application")
your_input = st.text_input(
	"Input:- ",
	"What is Generative AI?")  # sample input passed to help user what to ask
submit = st.button("Ask the question")

# when submit is clicked
if submit:
	response = get_gemini_response(your_input)
	st.subheader("The response is:- ")
	st.write(response)
