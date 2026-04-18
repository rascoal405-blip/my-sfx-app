import streamlit as st

st.set_page_config(page_title="صائد المؤثرات الذكي", layout="wide")

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

# روابط عالمية مفتوحة (Wikimedia Commons) - تعمل 100%
fx_data = [
    {"title": "صوت رعد (Thunder Sound)", "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Thunder_close_1.ogg"},
    {"title": "تنبيه رقمي (Digital Notification)", "url": "https://upload.wikimedia.org/wikipedia/commons/2/21/Incoming_message.ogg"},
    {"title": "صوت كيبورد (Keyboard Typing)", "url": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_on_a_computer_keyboard.ogg"}
]

for fx in fx_data:
    st.subheader(f"🎵 {fx['title']}")
    # مشغل الصوت (يدعم ملفات OGG و MP3)
    st.audio(fx['url'])
    # زر التحميل
    st.markdown(f'<a href="{fx["url"]}" target="_blank" class="download-btn">⬇️ اضغط هنا للتحميل المباشر</a>', unsafe_allow_html=True)
    st.divider()
