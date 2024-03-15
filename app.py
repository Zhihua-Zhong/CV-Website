from pathlib import Path
import streamlit as st
from PIL import Image
import yaml


def load_yml(path):
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
    return yml


# get OS path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'CV.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'
biography_path = current_dir / 'config' / 'biography.yml'
achievements_path = current_dir / 'config' / 'achievements.yml'

# load yml file
biography_yml = load_yml(biography_path)
achievements_yml = load_yml(achievements_path)

# initialize streamlit, load css, pdf, and profile picture
PAGE_TITLE = 'Digital CV | ' + biography_yml['name']
PAGE_ICON = ':wave:'
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# basic information section
name = biography_yml['name']
description = biography_yml['description']
email = biography_yml['email']
col1, col2 = st.columns([1, 2], gap='small')
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(name)
    st.write('Doctoral student at ***Tokyo Institude of Technology*** ')
    st.write('\n JSPS (DC) 日本学術振興特別研究員 ')
    st.write('\n Major: School of Computing, Artificial Intelligence')
    st.write('\n Interested research direction: Algorithms, Information fusion, Optimization modeling (e.g. Machine/Deep/Reinforcement learning, Huristic algorithms)')
    st.download_button(
        label='📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write('📫', email)

# social link section
social_media = biography_yml['social_media']
st.write('\n')
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')


# article publication
st.write('\n')
st.subheader('Academic Article Publication History')
st.write('---')
papers_dict = achievements_yml['papers']
for project, link in papers_dict.items():
    st.write(f"[{project}]({link})")
st.write('\n')

# conference presentation
st.subheader('Presentation on Academic Conference')
st.write('---')
presentation_dict = achievements_yml['presentation']
for index, conference in presentation_dict.items():
    st.write(f'{index} {conference}')

# grant, award, and qualification section
st.write('\n')
st.subheader('Grant, Award, & Qualification')
st.write('---')
grant_award_qualification = achievements_yml['grant_award_qualification']
for type_head, content in grant_award_qualification.items():
    st.write(f'🏆️{type_head}: {content}')


# experience section
st.write('\n')
st.subheader('Experience History')
st.write('---')
# doctoral education
st.write('🏆', '**Doctoral education at Tokyo Institute of Technology**')
st.write('09/2022 - Present')
st.write(
'''
- [Internship, 2023/11-2024/1] 5. Internship of company Sony: Develop a website to interact with, train the prediction model online and present the result of the data analysis.
- [Joint Research, 2023/4-2024/1] 4. Joint Research with company Sony: Analyse the sales data of Sony’s products, such as TVs and cameras, and predict the units and price of sales to solve the supply chain problem.
- [Presentation, 2023/9] 3. Presentation to Physical Society of Japan (日本物理学会) about 'Electric circuit network description of urban human mobility based on GPS data.'
- [Presentation, 2023/8] 2. Presentation to Statphys28 (International academic conference) about 'An analysis of human flow pattern based on Revised Electric Circuit Model.'
- [GPA] 1. Major GPA so far: 3.8/4.5.
'''
)
# --- master's education
st.write('\n')
st.write('🏆', '**Master\'s education at Jinan University**')
st.write('09/2019 - 07/2022')
st.write(
'''
- [R&D] Developed a machine learning model to predict the probability of gaining a certain disease based on the biochemical data from the patients (Publication [1]). 
- [R&D] Discovered the relationship between biochemical indexes, drug, and death ratio to give people a deeper understanding of diseases in medical science (Publication [2-4]).
- [R&D] Developed a Windows 10 software for paper [1] based on C++ and Python.
- [R&D] Developed a website using Java and Python to implement real-time patient prediction for paper[1].
- [GPA] Major GPA: 88/100, top 10%.
'''
)

# hard skill
st.subheader("Hard Skills")
st.write('---')
st.write(
        '''
        - 💻 Programming: Python (Scikit-learn, Pandas, Streamlit), Java (Spring)
        - 📚 Speciality: Algorithm, including: Machine learning, Deep learning, and Statistics
        - 🗄️ Databases: Postgres, MySQL
        '''
        )

# subject section
st.write('\n')
st.subheader('**Subjects good at teach**')
st.write('---')
st.write(
'''
1. Mathematics series: Calculus, Linear Algebra, and Statistics. 
2. Computer Science series: Python Programming, Java Programming, Data Structure and Algorithm, Database, and Machine Learning.)
'''
)
