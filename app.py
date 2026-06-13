import streamlit as st
import pandas as pd
import joblib

st.title("🌍 Air Quality Predictor")
st.write("Прогноз индекса качества воздуха (AQI) на основе уровней загрязнителей")

model = joblib.load('aqi_model.pkl')

pm25 = st.slider("PM2.5", 0.0, 500.0, 50.0)
pm10 = st.slider("PM10", 0.0, 500.0, 80.0)
no = st.slider("NO", 0.0, 100.0, 10.0)
no2 = st.slider("NO2", 0.0, 100.0, 20.0)
nox = st.slider("NOx", 0.0, 100.0, 20.0)
nh3 = st.slider("NH3", 0.0, 100.0, 10.0)
co = st.slider("CO", 0.0, 50.0, 1.0)
so2 = st.slider("SO2", 0.0, 100.0, 10.0)
o3 = st.slider("O3", 0.0, 200.0, 30.0)
benzene = st.slider("Benzene", 0.0, 50.0, 1.0)
toluene = st.slider("Toluene", 0.0, 50.0, 1.0)
xylene = st.slider("Xylene", 0.0, 50.0, 1.0)

if st.button("Предсказать AQI"):
    data = pd.DataFrame([[pm25,pm10,no,no2,nox,nh3,co,so2,o3,benzene,toluene,xylene]],
                         columns=['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'])
    pred = model.predict(data)[0]
    st.write(f"### Предсказанный AQI: {pred:.1f}")

    if pred <= 50:
        st.success("Хорошее качество воздуха ✅")
    elif pred <= 100:
        st.warning("Умеренное загрязнение ⚠️")
    elif pred <= 200:
        st.warning("Плохо для чувствительных групп 😷")
    else:
        st.error("Опасный уровень загрязнения! 🚨")
