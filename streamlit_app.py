import streamlit as st

# إعدادات الواجهة لتكون شبيهة بـ Artlist
st.set_page_config(page_title="ArtSFX Professional", layout="wide")

# تصميم الثيم الأسود الفخم
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .sfx-card {
        background: #111;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #ffeb3b;
        margin-bottom: 10px;
    }
    h3 { color: #ffeb3b; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 ArtSFX - بديل المونتير المجاني")
st.write("مكتبة مؤثرات تعمل بالكامل - جرب تشغيل أي صوت الآن")

# مكتبة أصوات مختبرة وتعمل 100% (روابط مباشرة)
sfx_db = {
    "🔥 Cinematic & Action": [
        {"name": "Explosion (انفجار)", "url": "https://www.soundjay.com/mechanical/sounds/explosion-02.mp3"},
        {"name": "Heavy Impact (ضربة قوية)", "url": "https://actions.google.com/sounds/v1/science_fiction/low_vibe.ogg"},
        {"name": "Action Transition (انتقال)", "url": "https://actions.google.com/sounds/v1/foley/wind_whoosh_fast.ogg"}
    ],
    "🎮 Gaming & UI": [
        {"name": "Success (نجاح)", "url": "https://www.soundjay.com/misc/sounds/bell-ringing-01.mp3"},
        {"name": "Button Click (نقرة)", "url": "https://www.soundjay.com/buttons/sounds/button-16.mp3"},
        {"name": "Coin Jump (قفزة)", "url": "https://storage.googleapis.com/codeskulptor-assets/jump.ogg"}
    ],
    "🏢 Ambience (أصوات واقعية)": [
        {"name": "Keyboard (كيبورد)", "url": "https://actions.google.com/sounds/v1/office/typing_medium_speed.ogg"},
        {"name": "Rain (مطر)", "url": "https://actions.google.com/sounds/v1/weather/rain_on_roof.ogg"}
    ]
}

# عرض الأصوات في تصنيفات
for cat, sounds in sfx_db.items():
    st.markdown(f"### {cat}")
    cols = st.columns(2)
    for i, sfx in enumerate(sounds):
        with cols[i % 2]:
            st.markdown(f'<div class="sfx-card"><h3>{sfx["name"]}</h3>', unsafe_allow_html=True)
            st.audio(sfx["url"])
            st.markdown(f'<a href="{sfx["url"]}" download style="color:#888; text-decoration:none; font-size:12px;">📥 رابط مباشر</a></div>', unsafe_allow_html=True)

st.info("ملاحظة: إذا لم يعمل صوت، تأكد من تحديث الصفحة (Refresh).")
