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
        color: #ffffff;
        text-shadow: 2px 2px 8px #ff7f50;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
    }
    textarea {
        border-radius: 10px;
        border: 2px solid #FF8C00 !important;
    }

    /* Translated text box ko dark karne ke liye */
    .stMarkdown div[data-testid="stMarkdownContainer"] p, 
    .stWrite {
        background-color: #1e293b; /* Dark Slate color */
        color: #ffffff !important; /* White text */
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #475569;
    }

    /* st.info (Notification) ko dark aur white text dene ke liye */
    div[data-testid="stNotification"] {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 10px;
        border: 1px solid #475569;
    }
    
    /* Icon ka color bhi white karne ke liye */
    div[data-testid="stNotification"] svg {
        fill: #ffffff !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div style="font-size:40px; text-align:center;">✨ 💛 ✨ 💛 ✨ 💛 ✨</div>', unsafe_allow_html=True)
st.markdown("<h1>Welcome to Your Multi-Language Translator</h1>", unsafe_allow_html=True)

# Translation logic using deep-translator
translator = GoogleTranslator()
langs_dict = translator.get_supported_languages(as_dict=True)
languages = {name.title(): code for name, code in langs_dict.items()}

text_to_translate = st.text_area("Enter text to translate:")

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
            
            # Using st.info which is now styled as dark with white text
            st.info(result)
            
            st.download_button(label="📋 Copy Translation", data=result, file_name="translation.txt")
        except Exception as e:
            st.error("Error: Could not translate text.")
