# ui/components/chat_bubble.py
import streamlit as st

def render_chat_bubble(message, sender="user"):
    """
    Render a chat message bubble
    sender: 'user' or 'ai'
    """
    if sender == "user":
        color = "#0B8F4D"      # DS Group primary color
        align = "right"
    else:
        color = "#F0F0F0"
        align = "left"

    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: {align};
            margin: 5px 0;
        ">
            <div style="
                background-color: {color};
                color: {'white' if sender=='user' else 'black'};
                padding: 12px;
                border-radius: 12px;
                max-width: 70%;
                word-wrap: break-word;
                font-family: 'Inter', sans-serif;
            ">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
