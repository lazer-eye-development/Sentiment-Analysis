import streamlit as st
import os
import json
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def perform_sentiment_analysis(text, input_type, model="gpt-4o"):
    """
    Perform sentiment analysis using OpenAI models.
    
    Args:
        text (str): The text to analyze
        input_type (str): The type of input (review, survey, social media)
        model (str): The OpenAI model to use
        
    Returns:
        str: Analysis result
    """
    try:
        # Create a prompt for sentiment analysis specific to packaging design
        prompt = f"Please perform sentiment analysis on the following {input_type} and identify key themes related to packaging design:\n\n{text}"
        
        # Call the OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a sentiment analysis expert specializing in consumer packaging feedback. Analyze the sentiment and identify key themes related to packaging design. Structure your response with clear sections for Sentiment Overview, Key Themes, and Recommendations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        
        # Extract the analysis result
        analysis_result = response.choices[0].message.content
        return analysis_result
    
    except Exception as e:
        logger.error(f"Error performing sentiment analysis: {e}")
        return f"An error occurred during sentiment analysis: {str(e)}"

def main():
    st.set_page_config(
        page_title="Consumer Sentiment Analysis for Packaging",
        page_icon="📊",
        layout="wide"
    )
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #2e6c80;
        }
        .stTextArea > div > div > textarea {
            background-color: #f8f9fa;
            color: #000000;  /* Ensure text is black for visibility */
            font-size: 16px; /* Increase font size for better readability */
        }
        .stButton button {
            background-color: #2e6c80;
            color: white;
        }
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Consumer Sentiment Analysis for Packaging")
    st.markdown("### Analyze feedback to improve packaging design decisions")
    
    # Model selection
    model_options = ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
    col1, col2 = st.columns([3, 1])
    
    with col2:
        selected_model = st.selectbox("Select OpenAI Model", model_options)
        
        # Save button
        if st.button("📋 Load Sample Data"):
            st.session_state.review_text = """
"I love the sleek and modern design of the packaging. It really stands out on the shelf and makes the product look premium."
"The packaging is way too bulky and difficult to open. It's frustrating and feels like a waste of materials."
"I appreciate the eco-friendly packaging. It's great to see companies prioritizing sustainability."
"The packaging doesn't provide enough information about the product. I had to search online to find the details I needed."
"The color scheme and branding on the packaging are eye-catching and memorable. It definitely grabs my attention."
"""
            st.session_state.survey_text = """
"I prefer packaging that is easy to open and reseal. Convenience is key for me."
"I'm willing to pay a bit more for packaging that is environmentally friendly and recyclable."
"Clear and concise product information on the packaging is a must. I don't want to have to guess what I'm buying."
"Packaging that is reusable or has multiple purposes is a big plus in my book."
"I tend to gravitate towards packaging designs that are minimalist and clean-looking."
"""
            st.session_state.social_text = """
"Just received my order, and I'm blown away by the stunning packaging design! It's almost too pretty to open. 😍 #unboxing #packaginggoals"
"Another company using excessive packaging materials. 😡 When will they learn that less is more? #wasteful #sustainability"
"Loving the new packaging update from my favorite brand! The colors are so vibrant, and it's much easier to open now. 👌 #packagedesign #userexperience"
"Had to spend 10 minutes trying to figure out how to open this package. 😓 Why do companies make it so complicated? #frustrated #packaging"
"Can we take a moment to appreciate the creativity and attention to detail in this packaging? It tells a story and creates an emotional connection. 🎉 #brandstorytelling #packagingdesign"
"""
            st.rerun()
                
        # Clear button
        if st.button("🧹 Clear All"):
            st.session_state.review_text = ""
            st.session_state.survey_text = ""
            st.session_state.social_text = ""
            st.session_state.review_analysis = None
            st.session_state.survey_analysis = None
            st.session_state.social_analysis = None
            st.rerun()
    
    with col1:
        # Initialize session state variables
        if "review_text" not in st.session_state:
            st.session_state.review_text = ""
        if "survey_text" not in st.session_state:
            st.session_state.survey_text = ""
        if "social_text" not in st.session_state:
            st.session_state.social_text = ""
            
        if "review_analysis" not in st.session_state:
            st.session_state.review_analysis = None
        if "survey_analysis" not in st.session_state:
            st.session_state.survey_analysis = None
        if "social_analysis" not in st.session_state:
            st.session_state.social_analysis = None
        
        # Input fields
        tab1, tab2, tab3 = st.tabs(["📝 Consumer Reviews", "📊 Survey Responses", "💬 Social Media"])
        
        with tab1:
            st.session_state.review_text = st.text_area(
                "Enter consumer reviews about packaging designs:",
                value=st.session_state.review_text,
                height=200
            )
            
        with tab2:
            st.session_state.survey_text = st.text_area(
                "Enter survey responses about packaging designs:",
                value=st.session_state.survey_text,
                height=200
            )
            
        with tab3:
            st.session_state.social_text = st.text_area(
                "Enter social media comments about packaging designs:",
                value=st.session_state.social_text,
                height=200
            )
    
    # Analysis button
    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        any_input = False
        
        if st.session_state.review_text:
            any_input = True
            with st.spinner("Analyzing sentiment for reviews..."):
                st.session_state.review_analysis = perform_sentiment_analysis(
                    st.session_state.review_text, 
                    "consumer review",
                    selected_model
                )
        
        if st.session_state.survey_text:
            any_input = True
            with st.spinner("Analyzing sentiment for survey responses..."):
                st.session_state.survey_analysis = perform_sentiment_analysis(
                    st.session_state.survey_text, 
                    "survey response",
                    selected_model
                )
        
        if st.session_state.social_text:
            any_input = True
            with st.spinner("Analyzing sentiment for social media comments..."):
                st.session_state.social_analysis = perform_sentiment_analysis(
                    st.session_state.social_text, 
                    "social media comment",
                    selected_model
                )
        
        if not any_input:
            st.warning("Please enter text in at least one of the input fields to analyze.")
    
    # Display analysis results
    if st.session_state.review_analysis or st.session_state.survey_analysis or st.session_state.social_analysis:
        st.markdown("## Analysis Results")
        
        result_tabs = st.tabs(["📝 Reviews Analysis", "📊 Survey Analysis", "💬 Social Media Analysis", "📋 Combined Insights"])
        
        with result_tabs[0]:
            if st.session_state.review_analysis:
                st.markdown(st.session_state.review_analysis)
            else:
                st.info("No review text analyzed yet.")
                
        with result_tabs[1]:
            if st.session_state.survey_analysis:
                st.markdown(st.session_state.survey_analysis)
            else:
                st.info("No survey responses analyzed yet.")
                
        with result_tabs[2]:
            if st.session_state.social_analysis:
                st.markdown(st.session_state.social_analysis)
            else:
                st.info("No social media comments analyzed yet.")
                
        with result_tabs[3]:
            if any([st.session_state.review_analysis, st.session_state.survey_analysis, st.session_state.social_analysis]):
                # Generate combined insights
                combined_prompt = "Based on the following analyses of packaging feedback, provide an overall summary of key insights and recommendations:\n\n"
                
                if st.session_state.review_analysis:
                    combined_prompt += f"CONSUMER REVIEWS ANALYSIS:\n{st.session_state.review_analysis}\n\n"
                    
                if st.session_state.survey_analysis:
                    combined_prompt += f"SURVEY RESPONSES ANALYSIS:\n{st.session_state.survey_analysis}\n\n"
                    
                if st.session_state.social_analysis:
                    combined_prompt += f"SOCIAL MEDIA COMMENTS ANALYSIS:\n{st.session_state.social_analysis}\n\n"
                
                with st.spinner("Generating combined insights..."):
                    response = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": "system", "content": "You are a packaging design consultant who synthesizes consumer feedback into actionable insights."},
                            {"role": "user", "content": combined_prompt}
                        ],
                        max_tokens=1000,
                        temperature=0.3
                    )
                    combined_analysis = response.choices[0].message.content
                    st.markdown(combined_analysis)
                    
                    # Add download button for combined report
                    if st.button("📥 Download Full Report"):
                        report = f"""# Packaging Design Sentiment Analysis Report
                        
## Consumer Reviews Analysis
{st.session_state.review_analysis if st.session_state.review_analysis else "No review analysis performed."}

## Survey Responses Analysis
{st.session_state.survey_analysis if st.session_state.survey_analysis else "No survey analysis performed."}

## Social Media Comments Analysis
{st.session_state.social_analysis if st.session_state.social_analysis else "No social media analysis performed."}

## Combined Insights
{combined_analysis}
"""
                        st.download_button(
                            label="Download Report as Text",
                            data=report,
                            file_name="packaging_sentiment_analysis.txt",
                            mime="text/plain"
                        )
            else:
                st.info("No analyses available for combined insights.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Error running the application: {e}")
        st.error(f"An error occurred: {str(e)}")