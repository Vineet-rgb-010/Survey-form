import streamlit as st
from supabase import create_client

main_url = 'https://xvplyihnrndggpxrqowv.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh2cGx5aWhucm5kZ2dweHJxb3d2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEyNTA0NzUsImV4cCI6MjA4NjgyNjQ3NX0.zxq2zPNEOdOliujZcYX7_ZBuAknq35qq9qen_xSaQpo'

supabase = create_client(main_url, key)

# session state control
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:

    with st.form(key='user-input-form'):
        st.header("Basic survey")

        name = st.text_input(label='Your name')
        age = st.number_input(label='Your age', max_value=100, min_value=0)
        city = st.text_input(label='Your city')
        email = st.text_input(label='Your email')
        languages = st.radio(
            label='Which languages do you know from list below?',
            options=['Python','Java','C++','C'],
            index=None
        )
        food = st.multiselect(
            label='Choose from the below list',
            options=['Dosa','Chinese','Vadapav','Pani puri']
        )

        submit = st.form_submit_button("Submit")

    if submit:
        if name and city and languages and food and email:

            data = {
                'name': name,
                'age': age,
                'city': city,
                'languages': languages,
                'email': email,
                'food': ", ".join(food)  # convert list to string
            }

            supabase.table('survey_data').insert(data).execute()

            st.session_state.submitted = True
            st.rerun()

        else:
            st.error("Fill all the details please!")

else:
    st.balloons()
    st.title("🎉 Thank You!")
    st.write("Your response has been recorded successfully.")
    if st.button("Submit another response"):
        st.session_state.submitted = False
        st.rerun()

