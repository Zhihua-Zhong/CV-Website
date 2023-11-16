from pathlib import Path

import streamlit as st
from PIL import Image


# path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# initialization, load css, pdf, and profile picture
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# general setting
PAGE_TITLE = "Digital CV | Zhihua Zhong"
PAGE_ICON = ":wave:"
NAME = "ZHihua Zhong"
DESCRIPTION = """
Doctoral student at ***Tokyo Institude of Technology***
\n JSPS (DC) 日本学術振興特別研究員
\n Major: School of Computing, Artificial Intelligence
"""
EMAIL = "zhong.z.af@m.titech.ac.jp"
SOCIAL_MEDIA = {
    "My GitHub": "https://github.com/Zhihua-Zhong",
    "My Laboratory": "http://www.smp.dis.titech.ac.jp/en/"
}
PROJECTS = {
    "[5]. Zhong Zhihua, Hideki Takayasu, Misako Takayasu. Novel approaches to urban human mobility: a physical analogy of electric circuit network and resulting gravity relations based on GPS data": "",
    "[4]. Gao M*, Zhong Z*, Yue Y, Liu F. Correlation between glycaemic variability and prognosis in diabetic patients with CKD. Endokrynol Pol. 73(6):947-953 (2022).": "https://journals.viamedica.pl/endokrynologia_polska/article/view/EP.a2022.0092/70385",
    "[3]. Liu, S.*, Zhong, Z.* & Liu, F. Prognostic value of hyperuricemia for patients with sepsis in the intensive care unit [J]. Sci Rep 12, 1070 (2022).": "https://www.nature.com/articles/s41598-022-04862-3",
    "[2]. Huang Y*, Zhong Z*, Liu F. The Association of Coagulation Indicators and Coagulant Agents With 30-Day Mortality of Critical Diabetics [J]. Clin Appl Thromb Hemost. 27:10760296211026385 (2021 Jan-Dec).": "https://journals.sagepub.com/doi/full/10.1177/10760296211026385",
    "[1]. Zhong, Z., Yuan, X., Liu, S. et al. Machine learning prediction models for prognosis of critically ill patients after open-heart surgery [J]. Sci Rep 11, 3384 (2021).": "https://www.nature.com/articles/s41598-021-83020-7",
}

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# Academic article publication history
st.write('\n')
st.subheader("Academic Article Publication History")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
st.write('\n')
st.subheader("Presentation on Academic Conference")
st.write("---")
st.write(
"""
- [2]. Electric circuit network description of urban human mobility based on GPS data, Physical Society of Japan (日本物理学会; 2023/9).
- [1]. An analysis of human flow pattern based on Revised Electric Circuit Model, Statphys28 (2023/8).
"""
)


# --- SKILLS ---
st.subheader("Hard Skills")
st.write(
"""
- 💻 Programming: Python (Scikit-learn, Pandas, Streamlit), Java (Spring)
- 📚 Speciality: Algorithm, including: Machine learning, Deep learning, and Statistics
- 🗄️ Databases: Postgres, MySQL
"""
)

# --- Qualification, Award, & Grant ---
st.write('\n')
st.subheader("Grant, Award, & Qualification")
st.write(
"""
- 🏆️ [Grant] 1: JSPS (Japan Society for the Promotion of Science) Research Fellowship for Young Scientists (2023, Doctor, Japan)
- 🏆️ [Grant] 2: "Support for Pioneering Research Initiated by the Next Generation" by Japan Science and Technology Agency (Grant Number JPMJSP2106; 2022, Doctor, Japan)
- 🏆️ [Award] 3: Software Copyright (2021, Master, China)
- 🏆️ [Award] 4: China National Scholarship for graduate students (2021, Master, China)
- 🏆️ [Certificate] 5: TOEIC (English ability): 810/1000 (2021, Master)
- 🏆️ [Certificate] 6: JLPT N1 (Japanese ability): 140/180 (2021, Master)
"""
)

# --- ACADEMIC ARTICLE PUBLICATION HISTORY ---
st.write('\n')
st.subheader("Experience History")
st.write("---")

# --- doctoral education
st.write("🏆", "**Doctoral education at Tokyo Institute of Technology**")
st.write("09/2022 - Present")
st.write(
"""
- [Internship, 2023/11-present] 5. Internship of company Sony: Develop a website to interact with and present the result of the data analysis.
- [Joint Research, 2023/4-present] 4. Joint Research with company Sony: Analyse the sales data of Sony’s products, such as TVs and cameras, and predict the units and price of sales to solve the supply chain problem.
- [Presentation, 2023/9] 3. Presentation to Physical Society of Japan (日本物理学会) about 'Electric circuit network description of urban human mobility based on GPS data.'
- [Presentation, 2023/8] 2. Presentation to Statphys28 (International academic conference) about 'An analysis of human flow pattern based on Revised Electric Circuit Model.'
- [GPA] 1. Major GPA so far: 3.8/4.5.
"""
)

# --- master's education
st.write('\n')
st.write("🏆", "**Master's education at Jinan University**")
st.write("09/2019 - 07/2022")
st.write(
"""
- [1] Developed a machine learning model to predict the probability of gaining a certain disease based on the biochemical data from the patients (Publication [1]). 
- [2] Discovered the relationship between biochemical indexes, drug, and death ratio to give people a deeper understanding of diseases in medical science (Publication [2-4]).
- [3] Developed a Windows 10 software for paper [1] based on C++ and Python.
- [4] Developed a website using Java and Python to implement real-time patient prediction for paper[1].
- [5] Major GPA: 88/100, top 10%.
"""
)

# --- subject in charge:
st.write('\n')
st.subheader("**Subjects good at teach (担当できる科目)**")
st.write("---")
st.write(
"""
1. Mathematics series: Calculus, Linear Algebra, and Statistics. (数学系: 微積分、線形代数、及び統計学)
2. Computer Science series: Python Programming, Java Programming, Data Structure and Algorithm, Database, and Machine Learning. (情報工学系: Python プログラミング、Java プログラミング、データ構造とアルゴリズム、データベース、及び機械学習)
"""
)
