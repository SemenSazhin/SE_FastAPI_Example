import requests
import streamlit as st


def normalize_base_url(raw_url: str) -> str:
    url = raw_url.strip()
    if not url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"
    return url.rstrip("/")


st.set_page_config(page_title="FastAPI Sentiment UI", page_icon=":speech_balloon:")
st.title("FastAPI + Streamlit")
st.caption("Тестовый веб-интерфейс для endpoint /predict/")

raw_api_base_url = st.text_input("FastAPI URL", value="http://127.0.0.1:8000")
api_base_url = normalize_base_url(raw_api_base_url)
text = st.text_area("Текст для анализа", value="I love FastAPI!")

if st.button("Отправить"):
    if not api_base_url:
        st.warning("Введите корректный URL FastAPI сервиса.")
    elif not raw_api_base_url.strip():
        st.warning("Введите URL FastAPI сервиса.")
    elif not text.strip():
        st.warning("Введите текст для анализа.")
    else:
        predict_url = f"{api_base_url}/predict/"
        try:
            response = requests.post(
                predict_url,
                json={"text": text.strip()},
                timeout=20,
            )
            response.raise_for_status()
            st.success("Ответ получен")
            try:
                st.json(response.json())
            except ValueError:
                st.error("Сервис вернул ответ не в формате JSON.")
                st.code(response.text)
        except requests.RequestException as exc:
            st.error(f"Ошибка запроса: {exc}")
