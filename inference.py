import gradio as gr
import pdfplumber
import docx
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------- Resume Text Extract --------

def extract_text_from_pdf(file):
text = ""
with pdfplumber.open(file) as pdf:
for page in pdf.pages:
text += page.extract_text() or ""
return text

def extract_text_from_docx(file):
doc = docx.Document(file)
text = "\n".join([para.text for para in doc.paragraphs])
return text

def extract_resume_text(file):
if file.name.endswith(".pdf"):
return extract_text_from_pdf(file)
elif file.name.endswith(".docx"):
return extract_text_from_docx(file)
else:
return "Unsupported file format"

# -------- Cleaning --------

def clean_text(text):
text = text.lower()
text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
return text

# -------- ATS Score --------

def calculate_ats_score(resume_text, job_description):

```
resume = clean_text(resume_text)
jd = clean_text(job_description)

text = [resume, jd]

cv = CountVectorizer()
matrix = cv.fit_transform(text)

similarity = cosine_similarity(matrix)[0][1]

ats_score = round(similarity * 100, 2)

return ats_score
```

# -------- Missing Skills --------

def missing_keywords(resume_text, job_description):

```
resume_words = set(clean_text(resume_text).split())
jd_words = set(clean_text(job_description).split())

missing = jd_words - resume_words

return ", ".join(list(missing)[:20])
```

# -------- Main Function --------

def analyze_resume(file, job_description):

```
if file is None:
    return "Upload resume", "", ""

resume_text = extract_resume_text(file)

ats_score = calculate_ats_score(resume_text, job_description)

missing = missing_keywords(resume_text, job_description)

suggestions = "Add missing skills and align resume with job description."

return f"ATS Score: {ats_score}%", missing, suggestions
```

# -------- Gradio UI --------

with gr.Blocks() as demo:

```
gr.Markdown("# Resume ATS Analyzer")

file = gr.File(label="Upload Resume (PDF/DOCX)")
job_description = gr.Textbox(label="Job Description", lines=10)

btn = gr.Button("Analyze Resume")

ats_output = gr.Textbox(label="ATS Score")
missing_output = gr.Textbox(label="Missing Keywords")
suggestion_output = gr.Textbox(label="Suggestions")

btn.click(
    analyze_resume,
    inputs=[file, job_description],
    outputs=[ats_output, missing_output, suggestion_output]
)
```

demo.launch(server_name="0.0.0.0", server_port=7860)
