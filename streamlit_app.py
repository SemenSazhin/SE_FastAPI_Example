import requests
import streamlit as st


st.set_page_config(page_title="FastAPI Sentiment UI", page_icon=":speech_balloon:")
st.title("FastAPI + Streamlit")
st.caption("Тестовый веб-интерфейс для endpoint /predict/")

api_base_url = st.text_input("FastAPI URL", value="http://127.0.0.1:8000")
text = st.text_area("Текст для анализа", value="I love FastAPI!")

if st.button("Отправить"):
    if not text.strip():
        st.warning("Введите текст для анализа.")
    else:
        try:
            response = requests.post(
                f"{api_base_url.rstrip('/')}/predict/",
                json={"text": text},
                timeout=20,
            )
            response.raise_for_status()
            st.success("Ответ получен")
            st.json(response.json())
        except requests.RequestException as exc:
            st.error(f"Ошибка запроса: {exc}")
