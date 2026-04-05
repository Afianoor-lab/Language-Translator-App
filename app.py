# ===============================
# STREAMLIT BEAUTIFUL LANGUAGE TRANSLATOR
# ===============================

import streamlit as st
from googletrans import Translator

# Initialize Translator
translator = Translator()

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
    }

    /* Text area styling */
    textarea {
        border-radius: 10px;
        border: 2px solid #FF8C00;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌟 Decorative top sparkles / lights
st.markdown('<div class="decorative-lights">✨ 💛 ✨ 💛 ✨ 💛 ✨</div>', unsafe_allow_html=True)

# 🌟 Left and Right side decorations
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
text_to_translate = st.text_area("Enter text to translate:")

# Language Options (added Russian)
from googletrans import LANGUAGES

# Convert language codes to readable names
languages = {name.title(): code for code, name in LANGUAGES.items()}


# Dropdown for Source and Target Language
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select Source Language", options=list(languages.keys()))
with col2:
    target_lang = st.selectbox("Select Target Language", options=list(languages.keys()))

# Translate Button
if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter text to translate!")
    elif source_lang == target_lang:
        st.warning("Source and target language cannot be the same!")
    else:
        try:
            result = translator.translate(text_to_translate, src=languages[source_lang], dest=languages[target_lang])
            st.success("✅ Translation Completed!")
            st.subheader("Translated Text:")
            st.write(result.text)

            # Copy Button
            st.download_button(
                label="📋 Copy Translation",
                data=result.text,
                file_name="translation.txt"
            )

        except Exception as e:
            st.error("Error: Could not translate text.")
            st.write(e)
