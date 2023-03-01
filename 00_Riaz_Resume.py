# from plotly.express import timeline
import streamlit as st
# import pandas as pd
import streamlit.components.v1 as components
# from streamlit_timeline import timeline
from streamlit_timeline import timeline
import plotly.graph_objects as go
from ds_steps import *
from prfdata import *
# 
# 

st.set_page_config(
    page_title="Riaz Ahmed Resume",
    page_icon="👋",
    layout="wide"
)


st.title('Summary')
st.write('#### Riaz Ahmed')


components.html('''
<h2 align="justify" style="font-weight:normal"> Motivated Python Developer & Data Scientist skilled in 1) Data Analysis & Predictive Data Analysis (using <b>Machine Learning algorithms</b>), 2) Python data analysis libraries (Pandas, Numpy, Plotly, Scikit-learn, Seaborn, etc.), 3) Jupyter Notebook, JupyterLab, SageMaker Studio Lab, Google Colab, 4) Streamlit (to Develop shareable web apps in minutes), 5) Claris FileMaker Rapid Application Development, 6) SQL & Data Modeling, 7) Agile Software Development, 8) Software Prototyping & StoryBoarding, 9) UML & BPMN, 10) Software Testing & Quality Assurance, 11) Health Care Domain, 12) Health Informatics Domain, 13) Business Apps Domain </h2>
''',
height=220)


st.write('#### Coming soon: :hibiscus:')
st.write('#### YouTube Channel (Data Science using Python, FileMaker), Streamlit Apps !!')

url = "https://www.linkedin.com/in/riazahmedsg/"
st.sidebar.markdown("## [Linkedin Profile](%s)" % url)

# Download Resume Button
# pdfFileObj = open('Riaz Ahmed Resume.pdf', 'rb')
# st.sidebar.download_button('Download Resume',pdfFileObj,file_name='Riaz Ahmed Resume.pdf',mime='pdf')

resume = "https://docs.google.com/document/d/1k2JGHInYY8nxvJFTrFKJOM-YOTHyFu_TJ1QT-M1Iw34/edit?usp=sharing"
st.sidebar.markdown("## [Download Riaz Resume](%s)" % resume)

ml_apps = "https://riazahmedsg-streamlit2-streamlit-app-809dok.streamlit.app/"
st.sidebar.markdown("## [Sample ML App](%s)" % ml_apps)

# ml_apps = "https://docs.google.com/document/d/1D_9FuECYE1s91LZQtvaCR-r8_Dra80gbiCdIy2efwyc/edit?usp=sharing"

# st.sidebar.markdown('1. First item \n2. Second item \n3. Third item')
# Test
st.sidebar.write('### Wish to Connect')
# st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: riazahmedsg@iconixvav.com')
# pdfFileObj = open('FileMaker Resume - Riaz Ahmed.pdf', 'rb')

# st.sidebar.write('\n\n\n\n\n')
# txt = st.text_area('Text to analyze', value='It was the best of times')

#st.balloons()
# Display Data Science Pyramid
col1, col2, col3 = st.columns([1,4,1])

with col1:
    pass

with col2:
    st.header("Data Science / Data Analysis Pyramid")
    st.image("pyramid.jpg")

with col3:
    pass
# 

st.title('My Journey of Data Science - Timelines: :hibiscus:')

# Timeline commented
with open('timeline.json', "r") as f:
    data = f.read()
timeline(data, height=500)

# 
st.title('Technical Skills and Tools: ')
with st.expander("Click + to expand: ", expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Data Analysis - Pandas, Numpy, Plotly, Scikit-learn, Seaborn, etc.</li>
    <li>Machine Learning Algorithms <i>Scikit-Learn</i> and <i>TensorFlow</i></li>
    <li>Python-Streamlit (to Develop shareable web apps in minutes)</li>
    <li>FileMaker RAD Development (FileMaker Rel. 12 - 19) -- (7+ Years)</li>
    <li>Software Quality Analyst (Software Testing, <br>Software Quality Assurance) - 15+ Years</li>
    <li>Database Development (SQL, ERD) - 10 Yrs </li>
    <li>Agile Software Development (SCRUM <br>ICONIX, User Stories, Product Backlog, Sprint Backlog, Sprint execution)</li>
    <li>Object Oriented Software Engineering (UML, BPMN)</li>
    <li>UX Prototyping -- Axure RP, HTML/CSS, Tumult Hype</li>
    <li>Strategyzer Business Model Canvas</li>
    </ol>
    </h3>
    ''', height=255, scrolling=True)
# 
# Python Specific Skills
st.title('Python Programming Skills: ')
with st.expander(" Click + to expand: ",expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Vital Python 
        <ul>
            <li>Data Types</li>
            <li>Booleans and Conditionals</li>
            <li>Loops</li>
            
        </ul>
    </li>
    <li> Python Data Structures
        <ul>
            <li>List</li>
            <li>Matrix</li>
            <li>Tupules</li>
            <li>Dictionery</li>
            <li>Sets</li>
            <li>Strings</li>
        </ul>
    </li>
    <li> Python Programs 
        <ul>
            <li>Python Scripts and Modules </li>
            <li>Python Functions</li>
            <li>Variable Scope</li>
            <li>Lambda Functions</li>
            <li>Sets</li>
        </ul>
    </li>
    <li> Python – Classes and Methods
        <ul>
            <li>Define Class</li>
            <li>Class Methods</li>
            <li>Properties</li>
            <li>Inheritance</li>
        </ul>
    </li>
    <li> Python Libraries
        <ul>
            <li>Date & Times</li>
            <li>Pandas</li>
            <li>Numpy</li>
            <li>Matplotlib</li>
            <li><b>Streamlit</b></li>
        </ul>
    </li>
    <li> Advanced Topics
        <ul>
            <li>Regular Expressions</li>
            <li>Debugging</li>
            <li>Package Installation</li>
            <li>Source Management</li>
        </ul>
    </li>
    </ol>
    </h3>
    ''', height=255, scrolling=True)
# 
# Data Science Skills
st.title('Data Science / Analysis Skills: ')
with st.expander("Click + to expand: ",expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Pandas DataFrame 
        <ul>
            <li>Load dataframe with data</li>
            <li>Explore dataframe containing data</li>
            <li>Grabbing subsets of data</li>
            <li>Adding and Removing Data</li>
            <li>Combine DataFrames | Merge, Join, Concat, & Append</li>
        </ul>
    </li>
    <li> Data Wrangling with Pandas
        <ul>
            <li>Cleaning Data</li>
            <li>Reshaping Data</li>
            <li>Handling duplicate, missing,or invalid data</li>
            <li>Aggregating Data By Group</li>
        </ul>
    </li>
    <li> EDA (Exploratory Data Analysis - Visualizations 
        <ul>
            <li>Matplotlib </li>
            <li>Seaborn</li>
            <li>Plotly</li>
            <li>Graphviz</li>
            <li>Bokeh</li>
            <li>pydeck</li>
            <li>Map</li>
        </ul>
    </li>
    <li> Machine Learning with <i>Scikit-Learn</i> and <i>TensorFlow</i>
        <ul>
            <li>Preprocessing data
            <ul>
                <li>Training and Testing Data Sets</li>
                <li>Scaling and Centring data</li>
                <li>Imputing</li>
                <li>Transformations</li>
            </ul>
            </li>
            <li>Build Machine Models
                <ul>
                <li>Linear Regression</li>
                <li>Logistic Regression</li>
                <li>Clustering</li>
                <li>Random Forests</li>
                </ul>
            </li>
        </ul>
    </li>
    <li> Evaluate Model Performance
        <ul>
            <li>Confusion Matrix</li>
            <li>Precision</li>
            <li>Accuracy</li>
            <li>Recall</li>
            <li>Specificity</li>
            <li>F1 score</li>
            <li>Precision-Recall or PR curve</li>
            <li>ROC (Receiver Operating Characteristics) curve</li>
            <li>PR vs ROC curve</li>
            <li>Cross-Validation</li>
        </ul>
    </li>
    <li> Predictions
    </li>
    </ol>
    </h3>
    ''', height=255, scrolling=True)
#
skill_col_size = 5
st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size, gap="small")
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()



# st.subheader('Career snapshot')

st.subheader('Education 📖')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='paleturquoise',
                align='center',height=65,font_size=25),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='lavender',
               align='left',height=40,font_size=17))])

fig.update_layout(width=850, height=600)
st.plotly_chart(fig)


st.subheader('Project Achievements 🥇')
achievement_list = ''.join(['<li>'+item+'</li>' for item in info['achievements']])
st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)

st.subheader('Daily routine as Data Scientist')
st.graphviz_chart(graph)




