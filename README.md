# 🇰🇿 Kazakhstan Constitution AI Assistant (Gemini)
## Bazarova Zarema, Zhalgassova Saniya,Seisekeyeva Dariga - SE-2321



## Overview
This is a Streamlit-based AI assistant that uses Google's Gemini Pro to answer questions about the Constitution of Kazakhstan. Users can also upload their own `.pdf` or `.txt` files to include in the assistant's context.

---

## Screenshots

![image](https://github.com/user-attachments/assets/c4fbae8f-c87f-41cd-bc32-6a1c9ef24b64)
![image](https://github.com/user-attachments/assets/3d7c57cc-dae5-4e5e-8e0b-3d2c6802856b)

---

##  Features

- Ask natural language questions about the Constitution
- Upload `.pdf` or `.txt` documents to expand context
- Answers powered by **Gemini Pro (Google Generative AI)**
- Clean, responsive UI using **Streamlit**

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/zzarema/constitution-ai-4.git
cd AI-Document-Assistant


### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Make sure requirements.txt includes:
```bash 
streamlit
python-dotenv
google-generativeai
pypdf
``` 
### 3. Set up your API key
Create a .env file in the root folder and add your Gemini API key:
``` bash
GOOGLE_API_KEY=your_actual_api_key
```

### 4. Run the app
```bash
 python -m streamlit run app.py
```
Then open browser and go to: http://localhost:8501


## MIT License

Copyright (c) 2025 se2321

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
