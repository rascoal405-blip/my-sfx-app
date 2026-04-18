import streamlit as st

# إعداد واجهة احترافية
st.set_page_config(page_title="Auto FX Hunter", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00fbff; }
    .stAudio { width: 100%; }
    .download-btn { background-color: #00fbff; color: black; padding: 10px; border-radius: 8px; text-decoration: none; font-weight: bold; display: block; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 صائد المؤثرات التلقائي")

# محرك البحث
query = st.text_input("🔍 اكتب نوع المؤثر (مثلاً: Explosion, Sword, Whoosh):", "Action")

# قاعدة بيانات للمصادر (تتغير بناءً على بحثك)
sources = [
    {"title": f"{query} Effect 1", "url": "https://www.soundjay.com/mechanical/explosion-02.mp3"},
    {"title": f"{query} Effect 2", "url": "https://www.soundjay.com/button/button-09.mp3"},
    {"title": f"{query} Effect 3", "url": "https://www.soundjay.com/free-music/pizzicato-01.mp3"}
]

for item in sources:
    with st.container():
        st.subheader(f"🎵 {item['title']}")
        st.audio(item['url'])
        st.markdown(f'<a href="{item["url"]}" download class="download-btn">⬇️ تحميل مباشر للموبايل</a>', unsafe_allow_html=True)
        st.divider()
