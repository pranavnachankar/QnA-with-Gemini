# Q&A with Gemini ✏️🔆 📝 

### Objective : 
Create a `Streamlit` app that allows you to interact with Google's Gemini LLM and get **TEXT** responses to user input.

### Installation and Configuration :
- Install required liraries such as `streamlit`, `google.generativeai`.
- [Get an API key](https://ai.google.dev/tutorials/python_quickstart#setup_your_api_key) 🔑
- Make sure to set your Google API key in the `main.py` file by replacing `GOOGLE_API_KEY` with your actual API key.


### List Models :
- To see the available Gemini models, please follow the below code :
```
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
	print(m.name)
```
- For detailed information about the available models, see [Gemini models](https://ai.google.dev/models/gemini).


### Output :
- Check `Output` folder to see sample of Generative AI `gemini-pro` model.
- ![Sample Output 1](Output/sample1.png)
- ![Sample Output 2](Output/sample2.png)