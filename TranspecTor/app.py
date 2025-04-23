from fastai.vision.all import *
import streamlit as st
import pathlib
import plotly.express as px

# Path fix for Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

st.title("🚗✈️⛵ Transport Bashoratchi")

file = st.file_uploader("🖼️ Rasm yuklang", type=["jpg", "jpeg", "png"])
if file:
    st.image(file, caption="Yuklangan rasm", use_container_width =True)

    img = PILImage.create(file)
    model = load_learner('Transport.pkl')

    pred, pred_id, probs = model.predict(img)
    confidence = probs[pred_id].item()
    THRESHOLD = 0.7 

    if confidence < THRESHOLD:
        st.warning(f"⚠️ Model bu rasmga unchalik ishonmayapti. Ehtimol, bu Airplane, car va boat klaslariga tegishli emas.\n\n"
                   f"Taxmin: {pred} ({confidence*100:.1f}%)")
    else:
        st.success(f"✅ Bashorat: {pred}")
        st.info(f"Ehtimollik: {confidence*100:.1f}%")
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)
else:
    st.info("📤 Rasm yuklang, iltimos.")