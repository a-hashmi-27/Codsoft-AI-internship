# import streamlit as st
# from transformers import BlipProcessor, BlipForConditionalGeneration
# from PIL import Image

# # Page config
# st.set_page_config(page_title="CaptionCraft", page_icon="🖼️", layout="wide")

# # Custom Header
# col1, col2 = st.columns([1, 14])
# with col1:
#     pass
# with col2:
#     st.markdown(
#         """
#         <h1 style='color: rgb(34, 102, 227); font-size: 40px; font-family: Arial, sans-serif;'>
#             🖼️ CaptionCraft
#         </h1>
#         <h3 style='font-size: 16px; font-family: Arial, sans-serif;'>
#             AI-Powered Image Caption Generator using BLIP
#         </h3>
#         """,
#         unsafe_allow_html=True
#     )

# # Sidebar
# st.sidebar.title("📸 Welcome to CaptionCraft")
# # st.sidebar.markdown("Upload an image to generate social-media-style captions.")
# st.sidebar.markdown("🤖 Powered by BLIP Transformer from Salesforce.")
# st.sidebar.markdown("© 2025 CaptionCraft™")

# # Load BLIP model
# @st.cache_resource
# def load_blip_model():
#     processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
#     model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
#     return processor, model

# processor, model = load_blip_model()

# # Simple function to turn a description into a caption with hashtags
# def create_caption_with_hashtags(description):
#     keywords = [word for word in description.lower().split() if word.isalpha() and len(word) > 3]
#     hashtags = [f"#{word}" for word in keywords[:6]]  # up to 6 hashtags
#     base_tags = ["#CaptionCraft", "#captured", "#AI"]
#     all_tags = list(set(hashtags + base_tags))
#     caption = f"{description.capitalize()}. {' '.join(all_tags)}"
#     return caption

# # Main content
# uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     img = Image.open(uploaded_file).convert("RGB")
#     st.image(img, caption="📸 Uploaded Image", width=600)

#     if st.button("✨ Click to Generate Caption"):
#         with st.spinner("🤖 Analyzing image..."):
#             inputs = processor(images=img, return_tensors="pt")
#             output = model.generate(**inputs, max_length=10)
#             raw_caption = processor.decode(output[0], skip_special_tokens=True)
#             final_caption = create_caption_with_hashtags(raw_caption)

#         st.success("✅ Caption Generated Successfully!")
#         st.markdown("### 📝 AI-Generated Caption:")
#         st.info(final_caption)
#     else:
#         st.warning("👆 Click the button above to generate a caption.")
# else:
#     st.markdown("Upload an image from the Browse files to get started.")

# # Footer
# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown(
#     "<p style='text-align: center; color: #6c757d;'>© CaptionCraft™ 2025 | Powered by Salesforce BLIP</p>",
#     unsafe_allow_html=True
# )

import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Page config
st.set_page_config(page_title="CaptionCraft", page_icon="🖼️", layout="wide")

# Load BLIP model
@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip_model()

# Generate hashtags from keywords
def create_caption_with_hashtags(description):
    keywords = [word for word in description.lower().split() if word.isalpha() and len(word) > 3]
    hashtags = [f"#{word}" for word in keywords[:6]]
    base_tags = ["#CaptionCraft", "#captured", "#AI"]
    all_tags = list(set(hashtags + base_tags))
    caption = f"{description.capitalize()}. {' '.join(all_tags)}"
    return caption

# HOME PAGE
def home_page():
    st.markdown("### 📥 Upload an image and generate a caption")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="📸 Uploaded Image", width=500)

        if st.button("✨ Click to Generate Caption"):
            with st.spinner("🤖 Analyzing image..."):
                inputs = processor(images=img, return_tensors="pt")
                output = model.generate(**inputs, max_length=10)
                raw_caption = processor.decode(output[0], skip_special_tokens=True)
                final_caption = create_caption_with_hashtags(raw_caption)

            st.success("✅ Caption Generated Successfully!")
            st.markdown("### 📝 AI-Generated Caption:")
            st.info(final_caption)
        else:
            st.warning("👆 Click the button above to generate a caption.")
    else:
        st.markdown("Upload an image to get started.")

# ABOUT PAGE
def about_page():
    st.markdown("## About CaptionCraft")
    st.write("""
Welcome to **CaptionCraft** — an AI-powered image captioning tool using BLIP for vision and captioning.

→ **How It Works**:
- Uses the BLIP Transformer to describe your image
- Converts keywords into hashtags

---

**Project by:**  
Syed Abrar ul Haq Hashmi — 161020748308
""")

# SETUP SESSION STATE FOR NAVIGATION
if "page" not in st.session_state:
    st.session_state.page = "Home"

# SIDEBAR BUTTONS
st.sidebar.title("📸 CaptionCraft")
st.sidebar.title("Menu")
col1, col2 = st.sidebar.columns(2)  # Side-by-side layout
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("ℹ️ About"):
        st.session_state.page = "About"

st.sidebar.markdown("🤖 Powered by Salesforce BLIP")
st.sidebar.markdown("© 2025 CaptionCraft™")

# HEADER (Move "CaptionCraft" upwards)
col1, col2 = st.columns([1, 14])
with col1:
    pass
with col2:
    st.markdown(
        """
        <h1 style='color: rgb(34, 102, 227); font-size: 35px; font-family: Arial, sans-serif; margin-top: -10px;'>
            🖼️ CaptionCraft
        </h1>
        <h3 style='font-size: 16px; font-family: Arial, sans-serif;'>
            AI-Powered Image Caption Generator using BLIP
        </h3>
        """,
        unsafe_allow_html=True
    )

# RENDER CURRENT PAGE
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "About":
    about_page()

# FOOTER
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #6c757d;'>© CaptionCraft™ 2025 | Powered by Salesforce BLIP</p>",
    unsafe_allow_html=True
)
