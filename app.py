import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Learning System", layout="wide")

# Theme toggle
theme = st.sidebar.toggle("🌗 Dark Mode")

bg = "#0f172a" if theme else "#f1f5f9"
text = "white" if theme else "black"
card_bg = "#1e293b" if theme else "white"
st.markdown(f"""
 <style>
 [data-testid="stAppViewContainer"] {{
     background-color: {bg};
    color: {text};
 }}

 [data-testid="stHeader"] {{
     background-color: {bg};
 }}

 [data-testid="stSidebar"] {{
     background-color: {bg};
 }}

 h1, h2, h3, h4, p {{
     color: {text} !important;
 }}
</style>
 """, unsafe_allow_html=True)

st.title("𝖑𝖊𝖆𝖗𝖓𝖝𝖕𝖊𝖗𝖙✍  The Smart Learning Recommendation System")

# Banner
st.markdown("""
            
 <div style="padding:15px;border-radius:10px;
 background: linear-gradient(90deg, #6366f1, #8b5cf6);
 color:white;text-align:center;font-size:20px;">
 🚀 Personalized AI Learning Dashboard
 </div>


""", unsafe_allow_html=True)

# Data
# 
data = pd.DataFrame({
    "Course": [
        "Python Basics","Advanced Python","Data Analysis",
        "Web Development","React","Django",
        "Machine Learning","Deep Learning","AI Projects",
        "Cyber Security Basics","Ethical Hacking","Network Security"
    ],
    "Category": [
        "Python","Python","Python",
        "Web development","Web development","Web development",
        "AI (artificial intelligence)","AI (artificial intelligence)","AI(artificial intelligence)",
        "Cyber security","Cyber security","Cyber security",
       
    ],
    "Min Marks":[
        0,70,50,
        0,60,75,
        65,80,70,
        0,75,60,
        
    ],
     "Duration": [
        "4 weeks","6 weeks","5 weeks",
        "5 weeks","6 weeks","8 weeks",
        "7 weeks","10 weeks","6 weeks",
        "4 weeks","6 weeks","5 weeks"
        
    ]
    
})

# 
# Interest (upar)
st.markdown("<h3 style='color:#00ffcc;'><b><i>Your Interest</i></b></h3>", unsafe_allow_html=True)
# interest = st.selectbox("", ["Python","Web devlopment","AI(artificial intelligence)","Cyber secuirty","Mobile app development"])
interest = st.selectbox("", data["Category"].unique())

 # Marks (neeche)
st.markdown("<h3 style='color:#00ffcc;'><b><i>Your Marks</i></b></h3>", unsafe_allow_html=True)


st.markdown('<div style="width:50%; margin:auto;">', unsafe_allow_html=True)

marks = st.slider("", 0, 100, 50)

st.markdown('</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])




# Recommendation
if st.button(" Generate Smart Recommendations", use_container_width=True):
     st.success(f"✨ Based on your marks ({marks}), best courses for you:")

    #  filtered = data[(data["Category"]==interest) & (data["Min Marks"]<=marks)]
filtered = data[data["Category"] == interest]

# priority sort
filtered = filtered.sort_values(by="Min Marks")

# top 5 suggestions
filtered = filtered.head(5)
filtered = filtered.sort_values(by="Min Marks", ascending=False)

if not filtered.empty:
        cols = st.columns(2)
        for i,row in filtered.iterrows():
            with cols[i%2]:
                st.markdown(f"""
                <div style="padding:20px;border-radius:12px;
                 background-color:{card_bg};color:{text};
                box-shadow:0 4px 10px rgba(0,0,0,0.2);margin:10px;">
               <h3>{row['Course']}</h3>
               <p>📘 Category: {row['Category']}</p>
        
        <p>⏳ Duration: {row['Duration']}</p>
                 </div>
                 """, unsafe_allow_html=True)
else:
         st.warning("No courses found")

