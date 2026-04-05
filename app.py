import streamlit as st
from deep_translator import GoogleTranslator

# ===============================
# 🌟 Beautiful Front Page Styling
# ===============================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFD580 0%, #FFB347 50%, #FFC966 100%);
        background-size: 400% 400%;
        animation: gradientBG 20s ease infinite;
        color: #000000;
    }
    @keyframes gradientBG {
        0%{background-position:0% 50%}
        50%{background-position:100% 50%}
        100%{background-position:0% 50%}
    }
    h1, h3 {
        font-family: 'Segoe UI', Tahoma, sans-serif;
        color: #ffffff !important;
        text-shadow: 2px 2px 8px #ff7f50;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 10px 25px !important;
        border: none !important;
    }
    textarea {
        border-radius: 10px !important;
        border: 2px solid #FF8C00 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* --- NEW UPDATED TRANSLATED BOX STYLE --- */
    .result-box {
        background-color: #262730 !important; /* Matches Streamlit's dark selectbox background */
        color: #ffffff !important;           /* Pure white text */
        padding: 15px !important;
        border-radius: 10px !important;
        border: 1px solid #475569 !important;
        font-size: 18px !important;
        margin-bottom: 20px !important;
    }

    /* Safeguard for info boxes */
    div[data-testid="stNotification"] {
        background-color: #262730 !important;
        color: white !important;
        border-radius: 10px;
    }
    
    div[data-testid="stNotification"] svg {
        fill: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div style="font-size:40px; text-align:center;">✨ 💛 ✨ 💛 ✨ 💛 ✨</div>', unsafe_allow_html=True)
st.markdown("<h1>Welcome to Your Language Translator</h1>", unsafe_allow_html=True)

# Translation logic using deep-translator
translator = GoogleTranslator()
langs_dict = translator.get_supported_languages(as_dict=True)
languages = {name.title(): code for name, code in langs_dict.items()}

text_to_translate = st.text_area("Enter text to translate:", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select Source Language", options=list(languages.keys()), index=list(languages.keys()).index('English'))
with col2:
    target_lang = st.selectbox("Select Target Language", options=list(languages.keys()), index=list(languages.keys()).index('Urdu'))

if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter text to translate!")
    else:
        try:
            result = GoogleTranslator(source=languages[source_lang], target=languages[target_lang]).translate(text_to_translate)
            st.subheader("Translated Text:")
            
            # Displaying result in the custom dark box with white text
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
            
            st.download_button(label="📋 Copy Translation", data=result, file_name="translation.txt")
        except Exception as e:
            st.error("Error: Could not translate text.")
