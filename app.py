import streamlit as st

# Sample app images
app_images = {
    "App 1": "app1_image.png",
    "App 2": "app2_image.png",
    "App 3": "app3_image.png"
}

def main():
    st.set_page_config(layout="wide")  # Set wide layout for better column display

    # Sidebar
    st.sidebar.title("My Apps")
    # selected_app = st.sidebar.selectbox("Select App", list(app_images.keys()))

    # Main content area
    col1, col2 = st.columns(2)

    # Display app image in column 1
    with col1:
        st.image('images/streamlit-calculator.jpg', caption='Streamlit calculator', width=300)
        url = "https://goks19-calculator.streamlit.app/"
        st.markdown(f"[Click to view]({url})")

        st.image('images/unit_convertor.jpg', caption='Streamlit unit convertor', width=300)
        url = "https://goks-app-unit-convertor.streamlit.app/"
        st.markdown(f"[Click to view]({url})")


    with col2:
        st.image('images/number-guessing-game.jpg', caption='Number-guessing-game', width=550)
        url = "https://goks-number-guessing-game.streamlit.app/"
        st.markdown(f"[Click to view]({url})")

    # # Add other content or functionalities in column 2 (optional)
    # with col2:
    #     st.write("App description")
    #     # Add other elements like buttons, text, etc.

if __name__ == "__main__":
    main()
