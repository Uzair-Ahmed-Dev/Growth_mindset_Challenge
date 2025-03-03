import streamlit as st

st.title("Growth Mindset Tracker")
st.write("This is your personal growth mindset tracker app built using Streamlit!")

# یوزر سے گولز کا انپوٹ حاصل کریں (comma-separated)
goal_input = st.text_area("Enter your goals (comma-separated)", "")

if st.button("Track Goals"):
    # گولز کو الگ الگ کرنے کے لیے split اور strip استعمال کریں
    goals = [g.strip() for g in goal_input.split(',') if g.strip()]
    
    if not goals:
        st.write("Please enter at least one goal.")
    else:
        st.write("### Your Goals:")
        # ہر گول کے لیے ایک چیک باکس بنائیں اور اس کی اسٹیٹس محفوظ کریں
        goal_statuses = {}
        for goal in goals:
            # ہر گول کے لیے چیک باکس: اگر چیک باکس منتخب ہے تو گول مکمل ہے
            completed = st.checkbox(f"{goal}", key=goal)
            goal_statuses[goal] = "Completed" if completed else "Pending"
        
        st.write("### Goals Status:")
        for goal, status in goal_statuses.items():
            st.write(f"**{goal}**: {status}")
