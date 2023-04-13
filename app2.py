import streamlit as st

# Define the Streamlit app
def app():
    st.title('UMBC Invasive Species ID')

    # Embed the web component using an iframe
    st.markdown('<iframe src="https://plantnet.org/ai-taxonomist-demo/" '
                'style="width:400%; height:700px;"></iframe>',
                unsafe_allow_html=True)

if __name__ == '__main__':
    app()
