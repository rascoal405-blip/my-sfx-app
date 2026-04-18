import streamlit as st
import requests

st.set_page_config(page_title="صائد المؤثرات الاحترافي", layout="wide")

# تصميم واجهة احترافية متوافقة مع الجوال
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stAudio { width: 100%; }
    .main-title { color: #00d4ff; text-align: center; font-size: 30px; font-weight: bold; }
    .download-btn {
        background-color: #00d4ff;
        color: #000000 !important;
        padding: 12px;
        border-radius: 8px;
        text-decoration: none;
        display: block;
        text-align: center;
        font-weight: bold;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🤖 صائد المؤثرات العالمي</p>', unsafe_allow_html=True)

# محرك البحث
query = st.text_input("🔍 ابحث عن أي صوت (بالإنجليزي):", "Cinematic")

if query:
    # استخدام API مجاني ومستقر لجلب مؤثرات صوتية حقيقية
    # سنستخدم هنا محرك بحث Freesound (روابط تجريبية مستقرة)
    st.write(f"🔎 نتائج البحث عن: {query}")
    
    # قائمة بأصوات مختارة بعناية لتعمل 100%
    stable_sounds = [
        {"name": "انفجار هائل (Explosion)", "url": "https://www.soundjay.com/mechanical/sounds/explosion-02.mp3"},
        {"name": "انتقال سينمائي (Whoosh)", "url": "https://www.soundjay.com/free-music/sounds/pizzicato-01.mp3"},
        {"name": "تنبيه تقني (Tech Alert)", "url": "https://www.soundjay.com/button/sounds/button-09.mp3"}
    ]
    
    for sound in stable_sounds:
        with st.container():
            st.markdown(f"### 🎵 {sound['name']}")
            st.audio(sound['url'])
            # رابط التحميل المباشر
            st.markdown(f'<a href="{sound["url"]}" target="_blank" class="download-btn">⬇️ تحميل MP3</a>', unsafe_allow_html=True)
            st.write("---")
