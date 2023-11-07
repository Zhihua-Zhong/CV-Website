from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zhihua Zhong"
PAGE_ICON = ":wave:"
NAME = "ZHihua Zhong"
DESCRIPTION = """
Doctoral student at ***Tokyo Institude of Technology***
\n Major: School of Computing, Artificial Intelligence
"""
EMAIL = "zhong.z.af@m.titech.ac.jp"
SOCIAL_MEDIA = {
    "My GitHub": "https://github.com/Zhihua-Zhong",
    "My Laboratory": "http://www.smp.dis.titech.ac.jp/en/"
}
PROJECTS = {
    "[5] Zhong Zhihua, Hideki Takayasu, Misako Takayasu. Electric circuit network description of urban human mobility based on GPS data (under peer review)": "",
    "[4] Gao M*, Zhong Z*, Yue Y, Liu F. Correlation between glycaemic variability and prognosis in diabetic patients with CKD. Endokrynol Pol. 73(6):947-953 (2022).": "https://journals.viamedica.pl/endokrynologia_polska/article/view/EP.a2022.0092/70385",
    "[3] Liu, S.*, Zhong, Z.* & Liu, F. Prognostic value of hyperuricemia for patients with sepsis in the intensive care unit [J]. Sci Rep 12, 1070 (2022).": "https://www.nature.com/articles/s41598-022-04862-3",
    "[2] Huang Y*, Zhong Z*, Liu F. The Association of Coagulation Indicators and Coagulant Agents With 30-Day Mortality of Critical Diabetics [J]. Clin Appl Thromb Hemost. 27:10760296211026385 (2021 Jan-Dec).": "https://journals.sagepub.com/doi/full/10.1177/10760296211026385",
    "[1] Zhong, Z., Yuan, X., Liu, S. et al. Machine learning prediction models for prognosis of critically ill patients after open-heart surgery [J]. Sci Rep 11, 3384 (2021).": "https://www.nature.com/articles/s41598-021-83020-7",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


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
st.divider()


# --- SKILLS ---
st.subheader("Hard Skills")
st.write(
"""
- 💻 Programming: Python (Scikit-learn, Pandas, Streamlit), Java (Spring)
- 📚 Speciality: Machine learning, Deep learning, Statistics
- 🗄️ Databases: Postgres, MySQL
"""
)
st.divider()


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

# --- JOB 1
st.write("🏆", "**Doctoral education at Tokyo Institute of Technology**")
st.write("09/2022 - Present")
st.write(
"""
- [1] Analyse the sales data of Sony’s products, such as TV and camera, and predict the units and price of sales to solve the supply chain problem.
- [2] Sony internship.
- [3] Major GPA so far: 3.8/4.5
"""
)

# --- JOB 2
st.write('\n')
st.write("🏆", "**Master's education at Jinan University**")
st.write("09/2019 - 07/2022")
st.write(
"""
- [1] Developed a machine learning model to predict the probability of gaining a certain disease based on the biochemical data from the patients. (Publication 1)
- [2] Discovered the relationship between biochemical indexes, drug, and death ratio to give people a deeper understanding of the diseases. (Publication 2-4)
- [3] Developed a Windows 10 software for paper [1] based on C++ and Python.
- [4] Developed a website to realise real-time prediction for patients, based on Java and Python
- [5] Major GPA: 88/100, top 10%
"""
)