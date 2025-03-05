import streamlit as st
import zxcvbn
from zxcvbn import zxcvbn


def get_strength_icon(score):
    if score == 0:
        return "🔒 Weak"  
    elif score == 1:
        return "🛑 Fair"  
    elif score == 2:
        return "⚠️ Good"  
    elif score == 3:
        return "🛡️ Strong"
    elif score == 4:
        return "✅ Very Strong"  
    else:
        return "🔒 Weak"

st.title("Password Strength Meter ")


password = st.text_input("Enter your password", type="password")

if password:

    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    
    strength_icon = get_strength_icon(score)
    
    st.write(f"Password Strength: {strength_icon}")
    
    
    if feedback:
        st.write("Suggestions to improve your password:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")


if password:
    if score == 0:
        st.progress(20)
    elif score == 1:
        st.progress(40)
    elif score == 2:
        st.progress(60)
    elif score == 3:
        st.progress(80)
    elif score == 4:
        st.progress(100)
