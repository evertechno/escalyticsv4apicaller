import streamlit as st
import requests
import json

# URL of your Flask API deployed on Render
API_URL = "https://your-render-app-url/analyze-email"

# Streamlit App Configuration
st.set_page_config(page_title="Email Analysis", page_icon="📧", layout="wide")
st.title("📨 Email Analysis & Insights")

st.write("Paste your email content below, and we'll analyze it with AI!")

# Input field for the email content
email_content = st.text_area("📩 Paste your email content here:", height=200)

# Button to trigger analysis
if st.button("🔍 Analyze Email"):
    if email_content:
        try:
            # Prepare the payload for the API request
            payload = {"email_content": email_content}
            
            # Send the POST request to the Flask API
            response = requests.post(API_URL, json=payload)
            
            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                
                # Display the results
                st.subheader("📌 Email Analysis Results")
                if "summary" in data:
                    st.write("**Summary:**", data["summary"])
                if "response" in data:
                    st.write("**Suggested Response:**", data["response"])
                if "sentiment" in data:
                    sentiment = data["sentiment"]
                    st.write(f"**Sentiment:** {sentiment['label']} (Polarity: {sentiment['polarity']})")
                if "readability_score" in data:
                    st.write(f"**Readability Score:** {data['readability_score']} / 10")
                if "tone" in data:
                    st.write("**Tone:**", data["tone"])
                if "urgency" in data:
                    st.write("**Urgency Level:**", data["urgency"])
                if "tasks" in data:
                    st.write("**Actionable Tasks:**", data["tasks"])
                if "subject_recommendation" in data:
                    st.write("**Subject Recommendation:**", data["subject_recommendation"])
                if "category" in data:
                    st.write("**Category:**", data["category"])
                if "emotion" in data:
                    st.write("**Emotion Analysis:**", data["emotion"])
                if "spam_status" in data:
                    st.write("**Spam Status:**", data["spam_status"])
                if "root_cause" in data:
                    st.write("**Root Cause Analysis:**", data["root_cause"])
                if "grammar_issues" in data:
                    st.write("**Grammar & Spelling Issues:**", data["grammar_issues"])
                if "clarity_score" in data:
                    st.write("**Clarity Score:**", data["clarity_score"])
                if "best_response_time" in data:
                    st.write("**Best Time to Respond:**", data["best_response_time"])
                if "professionalism_score" in data:
                    st.write("**Professionalism Score:**", data["professionalism_score"])

            else:
                # Handle non-200 response status codes
                st.error(f"Error: Unable to process the email. Status Code: {response.status_code}")
                st.error(f"Message: {response.json().get('error', 'Unknown error occurred')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please paste email content before clicking 'Analyze Email'.")

