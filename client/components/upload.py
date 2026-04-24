import streamlit as st
from utils.api import upload_files_api

def render_uploader():

    uploaded_files = st.sidebar.file_uploader(
        "Upload multiple files",
        type=["txt", "pdf", "doc", "docx"],
        accept_multiple_files=True
    )

    if st.sidebar.button("Upload DB") and uploaded_files:
        response = upload_files_api(uploaded_files)
        if response.status_code == 200:
            st.sidebar.success("Uploaded successfully")
        else:
            st.sidebar.error(f"Error: {response.text}")