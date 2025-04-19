import streamlit as st
import requests

st.set_page_config(page_title="📬 Email Viewer", layout="centered")
st.title("📧 Secure Email Document Viewer")

base_url = "http://localhost:8000"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        res = requests.post(f"{base_url}/auth/login", json={"email": email, "password": password})
        if res.status_code == 200:
            st.success("Login successful!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if st.session_state.logged_in:
    st.subheader("📬 Your Emails")

    if st.button("Fetch Emails"):
        with st.spinner("Loading emails..."):
            try:
                emails = requests.get(f"{base_url}/mail/emails").json()
                for e in emails:
                    with st.expander(f"From: {e['sender']} | Subject: {e['subject']}"):
                        st.write(f"📅 Date: {e['timestamp']}")
                        if e["attachments"]:
                            st.markdown("📎 Attachments:")
                            for a in e["attachments"]:
                                st.markdown(f"- {a}")
                        else:
                            st.write("No attachments.")
            except Exception as err:
                st.error(f"Failed to fetch emails: {err}")
