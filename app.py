import streamlit as st
import os
from datetime import datetime
from marketing_crew import MarketingCrew

# Page Configuration
st.set_page_config(
    page_title="Marketing Crew",
    #page_icon="🚀",
    layout="wide",
)


st.title("🚀 Marketing Automation")
st.caption("CrewAI")

# Sidebar → USER INPUTS ONLY
with st.sidebar:
    st.header("📌 Product Details")
    product_name = st.text_input("Product Name")
    product_description=st.text_input("Product Description")
    target_audience=st.text_input("Target Audience")
    budget=st.text_input("Marketing Budget")

    run_btn=st.button("Run Crew")


# HELPERS
def normalize_name(name: str) -> str:
    return (
        name.lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("&", "")
    )

def show_files(folder_path: str, key_prefix: str, product_name: str):
    if not os.path.exists(folder_path):
        st.info("No files generated yet.")
        return

    normalized_product = normalize_name(product_name)

    matched_files = []

    for f in os.listdir(folder_path):
        if not f.endswith(".md"):
            continue

        normalized_file = normalize_name(f)

        if normalized_product in normalized_file:
            matched_files.append(f)

    if not matched_files:
        st.info("No files generated for this product.")
        return

    for idx, file in enumerate(sorted(matched_files)):
        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        st.download_button(
            label=f"⬇DOWNLOAD. {file}",
            data=content,
            file_name=file,
            mime="text/markdown",
            key=f"{key_prefix}_{idx}"
        )

# Run Crew (ONLY on Button Click)
if run_btn:
    if not all([product_name,product_description,target_audience,budget]):
        st.warning("Please fill all fields befor running the crew.")
    else:
        inputs = {
            "product_name": product_name,
            "product_description": product_description,
            "target_audience": target_audience,
            "budget": budget,
            "current_date": datetime.now().strftime("%Y-%m-%d"),
        }

        with st.spinner("Running Marketing Crew... This may take a few minutes."):
            crew=MarketingCrew()
            crew.marketing_crew().kickoff(inputs=inputs)

        st.success("✅ Marketing assets generated successfully!")

# Output Viewer
st.header("📂 Generated Marketing Assets")

BASE_PATH="resources/drafts"

tabs=st.tabs([
    "📊 Strategy",
    "🗓 Content Calendar",
    "📱 Social Posts",
    "📝 Blogs",
    "🎥 Reels",
])

#if product_slug:
with tabs[0]:
    show_files("resources/drafts","strategy",product_name)

with tabs[1]:
    show_files("resources/drafts","calendar",product_name)

with tabs[2]:
    show_files("resources/drafts/posts","posts",product_name)

with tabs[3]:
    show_files("resources/drafts/blogs","blogs",product_name)

with tabs[4]:
    show_files("resources/drafts/reels","reels",product_name)

#else:
 #   st.info("Run the crew to view generated content.")