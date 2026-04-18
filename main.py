import streamlit as st

st.set_page_config(page_title="صائد المؤثرات الذكي", layout="wide")

# واجهة مستخدم محسنة للهاتف
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #58a6ff; }
    .stAudio { width: 100%; border-radius: 15px; }
    .download-btn {
        background-color: #238636;
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        display: block;
        text-align: center;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 صائد المؤثرات الصوتي")

# روابط مباشرة تعمل 100% (من سيرفرات SoundJay)
fx_data = [
    {"title": "انفجار قوي (Explosion)", "url": "https://www.soundjay.com/mechanical/sounds/explosion-02.mp3"},
    {"title": "انتقال سريع (Whoosh)", "url": "https://www.soundjay.com/free-music/sounds/pizzicato-01.mp3"},
    {"title": "ضغطة زر (Interface)", "url": "https://www.soundjay.com/button/sounds/button-3.mp3"}
]

for fx in fx_data:
    st.subheader(f"🎵 {fx['title']}")
    # مشغل الصوت
    st.audio(fx['url'])
    # زر تحميل حقيقي يفتح الملف للتحميل
    st.markdown(f'<a href="{fx["url"]}" target="_blank" class="download-btn">⬇️ اضغط هنا لتحميل MP3</a>', unsafe_allow_html=True)
    st.divider()
