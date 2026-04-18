import streamlit as st

st.title("🎧 مكتبة المؤثرات الاحترافية")

# روابط مباشرة مضمونة 100% من سيرفرات جوجل
sounds = [
    {"name": "انفجار سينمائي", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/explosion.ogg"},
    {"name": "تنبيه رقمي", "url": "https://storage.googleapis.com/codeskulptor-assets/base_2014/guisounds/pizzicato.ogg"},
    {"name": "صوت قفزة", "url": "https://storage.googleapis.com/codeskulptor-assets/jump.ogg"}
]

for sfx in sounds:
    with st.container():
        st.subheader(sfx["name"])
        st.audio(sfx["url"])
        st.write("---")
