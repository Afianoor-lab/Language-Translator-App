# ===============================
# STREAMLIT BEAUTIFUL LANGUAGE TRANSLATOR
# ===============================

import streamlit as st
from googletrans import Translator

# Initialize Translator
# NOTE: Using a try-except block for better stability on cloud deployment
try:
    translator = Translator()
except Exception:
    st.error("Translator initialization failed. Please refresh the page.")

# ===============================
# 🌟 Beautiful Front Page Styling
# ===============================
st.markdown(
    """
    <style>
    /* Page background gradient - fresh mustard/golden with colorful spark */
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

    /* Main headers styling */
    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #ffffff;
        text-shadow: 2px 2px 8px #ff7f50;
        text-align: center;
    }

    h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #ffffff;
        text-align: center;
    }

    /* Decorative sparkles / lights */
    .decorative-lights {
        font-size: 40px;
        text-align: center;
        animation: blink 1.2s infinite;
        color: #FFD700;
    }

    @keyframes blink {
        0% {opacity:1;}
        50% {opacity:0.3;}
        100% {opacity:1;}
    }

    /* Side decorations (left and right) */
    .side-decoration-left, .side-decoration-right {
        position: absolute;
        top: 100px;
        font-size: 30px;
        animation: blink 1.5s infinite;
        color: #ff69b4;
    }

    .side-decoration-left { left: 10px; }
    .side-decoration-right { right: 10px; }

    /* Stylish button */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 25px;
        box-shadow: 2px 2px 6px #888888;
        border: none;
    }

    /* Text area styling */
    textarea {
        border-radius: 10px;
        border: 2px solid #FF8C00 !important;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌟 Decorative elements
st.markdown('<div class="decorative-lights">✨ 💛 ✨ 💛 ✨ 💛 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="side-decoration-left">✨ 🌸 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="side-decoration-right">🌼 ✨ 🌸</div>', unsafe_allow_html=True)

# 🌟 Main App Title
st.markdown("<h1>Welcome to Your Language Translator</h1>", unsafe_allow_html=True)
st.markdown("<h3>Translate text into multiple languages!</h3>", unsafe_allow_html=True)
st.markdown("---")

# ===============================
# TRANSLATION FUNCTIONALITY
# ===============================

# Text Input
text_to_translate = st.text_area("Enter text to translate:", height=150)

# Language Options
from googletrans import LANGUAGES
languages = {name.title(): code for code, name in LANGUAGES.items()}

# Dropdown for Source and Target Language
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select Source Language", options=list(languages.keys()), index=list(languages.keys()).index('English') if 'English' in languages else 0)
with col2:
    target_lang = st.selectbox("Select Target Language", options=list(languages.keys()), index=list(languages.keys()).index('Urdu') if 'Urdu' in languages else 1)

# Translate Button
if st.button("Translate Now"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate!")
    elif source_lang == target_lang:
        st.warning("Source and target languages are the same!")
    else:
        try:
            with st.spinner('Translating...'):
                result = translator.translate(
                    text_to_translate, 
                    src=languages[source_lang], 
                    dest=languages[target_lang]
                )
                
            st.success("✅ Done!")
            st.markdown("### Translated Text:")
            st.info(result.text)

            # Download Button
            st.download_button(
                label="📋 Download as Text File",
                data=result.text,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error("Connection Error: Please try again in a moment.")
            # st.write(e) # Uncomment for debugging
