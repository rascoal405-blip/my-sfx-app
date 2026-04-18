import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="SFX Elite - مكتبة المؤثرات", page_icon="🎧", layout="wide")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stAudio { width: 100%; }
    .sfx-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00d4ff;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 SFX Elite - المكتبة الاحترافية للمونتاج")
st.write("مجموعة مختارة من أفضل المؤثرات الصوتية بجودة عالية")

# تقسيم المؤثرات إلى تصنيفات
tab1, tab2, tab3 = st.tabs(["🔥 سينمائي وانفجارات", "🎮 ألعاب وإلكتروني", "🔔 تنبيهات وواجهة"])

# قاعدة بيانات المؤثرات (روابط مباشرة مضمونة)
sfx_library = {
    "Cinematic": [
        {"name": "انفجار ضخم (Epic Explosion)", "url": "https://www.soundjay.com/mechanical/sounds/explosion-01.mp3"},
        {"name": "ضربة سينمائية (Cinematic Hit)", "url": "https://www.soundjay.com/free-music/sounds/action-climax-01.mp3"},
        {"name": "تراجع صوتي (Whoosh)", "url": "https://www.soundjay.com/free-music/sounds/fast-whoosh-01.mp3"},
        {"name": "صوت رعد (Thunder)", "url": "https://www.soundjay.com/nature/sounds/thunder-01.mp3"}
    ],
    "Gaming": [
        {"name": "قفزة سوبر ماريو", "url": "https://storage.googleapis.com/codeskulptor-assets/jump.ogg"},
        {"name": "عملة معدنية (Coin)", "url": "https://storage.googleapis.com/codeskulptor-assets/objects/coin_1.mp3"},
        {"name": "خسارة (Game Over)", "url": "https://www.soundjay.com/misc/sounds/fail-whistle-01.mp3"},
        {"name": "ليزر (Laser Shoot)", "url": "https://www.soundjay.com/mechanical/sounds/laser-gun-01.mp3"}
    ],
    "UI/Alerts": [
        {"name": "تنبيه رقمي (Digital Alert)", "url": "https://www.soundjay.com/communication/sounds/digital-beeping-01.mp3"},
        {"name": "نقر زر (Button Click)", "url": "https://www.soundjay.com/buttons/sounds/button-16.mp3"},
        {"name": "رسالة واردة", "url": "https://www.soundjay.com/communication/sounds/message-alert-01.mp3"}
    ]
}

# عرض المؤثرات في التبويبات
with tab1:
    for sfx in sfx_library["Cinematic"]:
        with st.container():
            st.markdown(f'<div class="sfx-card"><h3>{sfx["name"]}</h3></div>', unsafe_allow_html=True)
            st.audio(sfx["url"])
            st.write("---")

with tab2:
    for sfx in sfx_library["Gaming"]:
        with st.container():
            st.markdown(f'<div class="sfx-card"><h3>{sfx["name"]}</h3></div>', unsafe_allow_html=True)
            st.audio(sfx["url"])
            st.write("---")

with tab3:
    for sfx in sfx_library["UI/Alerts"]:
        with st.container():
            st.markdown(f'<div class="sfx-card"><h3>{sfx["name"]}</h3></div>', unsafe_allow_html=True)
            st.audio(sfx["url"])
            st.write("---")

st.info("نصيحة: يمكنك إضافة المزيد من الروابط داخل ملف الكود في أي وقت.")
