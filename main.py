import streamlit as st

st.set_page_config(page_title="صائد المؤثرات الذكي", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #58a6ff; }
    .stAudio { width: 100%; border-radius: 15px; background-color: #161b22; }
    .download-btn {
        background-color: #00fbff;
        color: black !important;
        padding: 15px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        display: block;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 صائد المؤثرات المباشر")

# روابط مباشرة 100% من سيرفرات جوجل العامة (Google Storage)
fx_data = [
    {"name": "انفجار قوي (Explosion)", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/explosion.ogg"},
    {"name": "تنبيه رقمي (Notification)", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/guisounds/pizzicato.ogg"},
    {"name": "صوت القفز (Jump Effect)", "url": "https://storage.googleapis.com/codeskulptor-assets/jump.ogg"}
]

for fx in fx_data:
    st.subheader(f"🎵 {fx['name']}")
    # تشغيل الصوت
    st.audio(fx['url'])
    # زر التحميل المباشر
    st.markdown(f'<a href="{fx["url"]}" target="_blank" class="download-btn">⬇️ اضغط هنا للتحميل فوراً</a>', unsafe_allow_html=True)
    st.write("---")
