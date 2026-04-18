import streamlit as st

# إعداد الصفحة بتصميم عريض واحترافي
st.set_page_config(page_title="المكتبة الاحترافية للمؤثرات", layout="wide")

# تصميم CSS لتحويل التطبيق لشكل سينمائي
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00d4ff; }
    .sfx-card {
        background: linear-gradient(145deg, #111, #1a1a1a);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #00d4ff;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        margin-bottom: 25px;
        text-align: center;
    }
    .download-link {
        background: #00d4ff;
        color: black !important;
        padding: 12px 25px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        transition: 0.3s;
    }
    .download-link:hover { background: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 SFX Master Pro")
st.write("---")

# مكتبة مؤثرات صوتية موسعة (تعمل 100% على الأندرويد)
sfx_library = [
    {"name": "انفجار عميق (Deep Explosion)", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/explosion.ogg"},
    {"name": "انتقال سريع (Fast Transition)", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/guisounds/pizzicato.ogg"},
    {"name": "صوت القفز (Jump Effect)", "url": "https://storage.googleapis.com/codeskulptor-assets/jump.ogg"},
    {"name": "محرك سيارة (Engine Run)", "url": "https://storage.googleapis.com/codeskulptor-assets/p_cars/engine_1.mp3"},
    {"name": "تنبيه رقمي (Digital Alert)", "url": "https://www.soundjay.com/button/sounds/button-09.mp3"},
    {"name": "صوت الكاميرا (Camera Click)", "url": "https://www.soundjay.com/mechanical/sounds/camera-shutter-click-01.mp3"}
]

# عرض الأصوات في شبكة احترافية (3 أعمدة)
cols = st.columns(3)
for i, sfx in enumerate(sfx_library):
    with cols[i % 3]:
        st.markdown(f'<div class="sfx-card">', unsafe_allow_html=True)
        st.markdown(f"### 🎵 {sfx['name']}")
        st.audio(sfx['url'])
        st.markdown(f'<a href="{sfx["url"]}" target="_blank" class="download-link">⬇️ تحميل مباشر</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.info("سيتم إضافة المزيد من الأصوات تلقائياً في التحديث القادم!")
