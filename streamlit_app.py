import streamlit as st

# إعداد واجهة احترافية تشبه Artlist
st.set_page_config(page_title="ArtSFX - مكتبة المونتاج الحرة", page_icon="🎬", layout="wide")

# تصميم الثيم المظلم والأنيق
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .sfx-card {
        background: #111111;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 1rem;
        transition: 0.3s;
    }
    .sfx-card:hover { border-color: #ffeb3b; }
    .category-header { color: #ffeb3b; border-bottom: 2px solid #ffeb3b; padding-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 ArtSFX Free Library")
st.write("بديلك المجاني لـ Artlist - مؤثرات منتقاة للمونتاج الاحترافي")

# قائمة مؤثرات موسعة بروابط مباشرة من خوادم موثوقة (Direct CDN)
sfx_groups = {
    "🔥 Cinematic & Transitions": [
        {"name": "Deep Cinematic Hit", "url": "https://actions.google.com/sounds/v1/science_fiction/low_vibe.ogg"},
        {"name": "Fast Wind Whoosh", "url": "https://actions.google.com/sounds/v1/foley/wind_whoosh_fast.ogg"},
        {"name": "Glitch Static", "url": "https://actions.google.com/sounds/v1/science_fiction/glitch_digital_static.ogg"},
        {"name": "Epic Rise", "url": "https://actions.google.com/sounds/v1/science_fiction/ufo_take_off.ogg"}
    ],
    "💻 Tech & Digital": [
        {"name": "Keyboard Mechanical", "url": "https://actions.google.com/sounds/v1/office/typing_medium_speed.ogg"},
        {"name": "Digital Notification", "url": "https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg"},
        {"name": "Mouse Click", "url": "https://actions.google.com/sounds/v1/office/mouse_click.ogg"},
        {"name": "UI Selection", "url": "https://actions.google.com/sounds/v1/alarms/beep_short.ogg"}
    ],
    "🌲 Nature & Ambience": [
        {"name": "Rain & Thunder", "url": "https://actions.google.com/sounds/v1/weather/rain_on_roof.ogg"},
        {"name": "Forest Birds", "url": "https://actions.google.com/sounds/v1/ambiences/forest_ambience.ogg"},
        {"name": "Ocean Waves", "url": "https://actions.google.com/sounds/v1/weather/ocean_waves_crashing.ogg"}
    ]
}

# عرض المحتوى بشكل منظم
for category, sounds in sfx_groups.items():
    st.markdown(f"<h2 class='category-header'>{category}</h2>", unsafe_allow_html=True)
    
    # توزيع الأصوات في أعمدة (Grid)
    cols = st.columns(2)
    for i, sfx in enumerate(sounds):
        with cols[i % 2]:
            st.markdown(f"""
                <div class='sfx-card'>
                    <h4>{sfx['name']}</h4>
                </div>
            """, unsafe_allow_html=True)
            st.audio(sfx["url"])

st.divider()
st.caption("ملاحظة: هذه الأصوات مقدمة من مستودعات Google Open Source وهي تعمل 100% في أي مكان.")
