import streamlit as st


st.write("""
         # Maximum of Three Numbers
         Displays the Maximum among the three inputs
         """)

st.subheader("Inputs:")
st.write("Number with upto 2 decimal precision points are supported!")

x = st.number_input("Input Number 1:", value=0.0000, step=0.01)
y = st.number_input("Input Number 2:", value=0.0000, step=0.01)
z = st.number_input("Input Number 3:", value=0.0000, step=0.01)


st.write(f'The Maximum of these values is:  {max(x, y, z)}')
