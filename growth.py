import streamlit as st

st.title("Growth Mindset Tracker")
st.write("This is your personal growth mindset tracker app built using Streamlit!")

# ی (comma-separated)
goal_input = st.text_area("Enter your goals (comma-separated)", "")

if st.button("Track Goals"):

    goals = [g.strip() for g in goal_input.split(',') if g.strip()]
    
    if not goals:
        st.write("Please enter at least one goal.")
    else:
        st.write("### Your Goals:")

        goal_statuses = {}
        for goal in goals:

            completed = st.checkbox(f"{goal}", key=goal)
            goal_statuses[goal] = "Completed" if completed else "Pending"
        
        st.write("### Goals Status:")
        for goal, status in goal_statuses.items():
            st.write(f"**{goal}**: {status}")
