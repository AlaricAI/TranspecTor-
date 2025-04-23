from fastai.vision.all import *
import streamlit as st
import plotly.express as px
import pathlib
import platform

# Windows uchun Path fix (faqat kerak bo‘lsa)
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

# Sarlavha
st.title("🚗✈️⛵ Transport Bashoratchi")

# Fayl yuklash
file = st.file_uploader("🖼️ Rasm yuklang", type=["jpg", "jpeg", "png"])

if file:
    # Yuklangan rasmni ko‘rsatish
    st.image(file, caption="Yuklangan rasm", use_container_width=True)

    # Modelni yuklash
    model = load_learner('Transport.pkl')

    # Rasmni yaratish va bashorat qilish
    img = PILImage.create(file)
    pred, pred_id, probs = model.predict(img)
    confidence = probs[pred_id].item()
    THRESHOLD = 0.7

    # Natijani chiqarish
    if confidence < THRESHOLD:
        st.warning(f"⚠️ Model bu rasmga ishonmayapti. Ehtimol, bu 'airplane', 'car', yoki 'boat' klaslariga tegishli emas.\n\n"
                   f"Taxmin: {pred} ({confidence*100:.1f}%)")
    else:
        st.success(f"✅ Bashorat: {pred}")
        st.info(f"Ehtimollik: {confidence*100:.1f}%")

    # Diagramma chizish
    fig = px.bar(
        x=probs.numpy()*100,
        y=model.dls.vocab,
        orientation='h',
        labels={'x': 'Ehtimollik (%)', 'y': 'Klasslar'},
        title="Klasslar bo‘yicha ehtimollik"
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)
else:
    st.info("📤 Rasm yuklang, iltimos.")
