import streamlit as st

# إعداد واجهة سينمائية احترافية
st.set_page_config(page_title="ArtSFX Pro", layout="wide")

# تصميم مستوحى من Artlist
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .sfx-card {
        background: #111;
        padding: 20px;
        border-radius: 12px;
        border-bottom: 3px solid #f39c12;
        margin-bottom: 15px;
    }
    h3 { color: #f39c12; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 ArtSFX: مكتبة المونتاج الاحترافية")
st.write("بديلك المجاني والأسرع لـ Artlist")

# مكتبة مؤثرات ضخمة (روابط مباشرة 100%)
sfx_categories = {
    "🔥 Cinematic (انفجارات وانتقالات)": [
        {"n": "Explosion Deep", "u": "https://www.soundjay.com/mechanical/sounds/explosion-01.mp3"},
        {"n": "Cinematic Whoosh", "u": "https://actions.google.com/sounds/v1/foley/wind_whoosh_fast.ogg"},
        {"n": "Heavy Thud", "u": "https://actions.google.com/sounds/v1/science_fiction/low_vibe.ogg"},
        {"n": "Glitch Transition", "u": "https://actions.google.com/sounds/v1/science_fiction/glitch_digital_static.ogg"}
    ],
    "🎮 Gaming & UI (ألعاب وواجهات)": [
        {"n": "Level Up Sync", "u": "https://www.soundjay.com/misc/sounds/bell-ringing-01.mp3"},
        {"n": "Digital Beep", "u": "https://www.soundjay.com/buttons/sounds/button-16.mp3"},
        {"n": "Success Chime", "u": "https://www.soundjay.com/misc/sounds/magic-chime-01.mp3"},
        {"n": "Coin Collect", "u": "https://storage.googleapis.com/codeskulptor-assets/objects/coin_1.mp3"}
    ],
    "🏢 Office & Nature (واقعي وطبيعة)": [
        {"n": "Keyboard Typing", "u": "https://actions.google.com/sounds/v1/office/typing_medium_speed.ogg"},
        {"n": "Rain & Thunder", "u": "https://actions.google.com/sounds/v1/weather/rain_on_roof.ogg"},
        {"n": "Camera Shutter", "u": "https://www.soundjay.com/mechanical/sounds/camera-shutter-click-01.mp3"}
    ]
}

# عرض الأصوات في شبكة (Grid)
for cat, sounds in sfx_categories.items():
    st.subheader(cat)
    cols = st.columns(2)
    for i, sfx in enumerate(sounds):
        with cols[i % 2]:
            st.markdown(f'<div class="sfx-card"><h3>{sfx["n"]}</h3>', unsafe_allow_html=True)
            st.audio(sfx["u"])
            st.markdown(f'<a href="{sfx["u"]}" target="_blank" style="color:#aaa;text-decoration:none;">📥 تحميل الملف</a></div>', unsafe_allow_html=True)

st.success("تم تحديث المكتبة بأحدث الروابط المباشرة!")
