# chatbot.py
# Core chatbot logic with JSON-based FAQ + rule-based intent detection

import json

# Load FAQ data from JSON file
with open('data/faq.json', 'r', encoding='utf-8') as f:
    faq_data = json.load(f)

# Function to search for a matching question in FAQ
def search_faq(user_input):
    user_input = user_input.lower()
    for item in faq_data:
        question = item["question"].lower()
        if question in user_input or user_input in question:
            return item["answer"]
    return None

# Function to handle rule-based keyword matching
def rule_based_response(user_input):
    user_input = user_input.lower()

    if "admission" in user_input or "apply" in user_input:
        return "You can apply for admissions online through our portal. Admissions are open for B.Tech, M.Tech, MBA, and more. Visit: /admissions"

    elif "courses" in user_input or "programs" in user_input:
        return "We offer B.Tech, M.Tech, BBA, MBA, B.Sc, and diploma programs across various departments."

    elif "eligibility" in user_input:
        return "Eligibility criteria differ by course. For B.Tech, you need a minimum of 60% in 12th grade with PCM subjects."

    elif "deadline" in user_input:
        return "The last date to apply for admissions is June 30th. Hurry up!"

    elif "fee" in user_input or "fees" in user_input or "tuition" in user_input:
        return "The tuition fee for B.Tech is ₹90,000 per year. Scholarships and installment options are available."

    elif "exam" in user_input and "schedule" in user_input:
        return "The semester exam schedule will be published on the student portal by May 1st."

    elif "results" in user_input:
        return "You can check your results on the university portal using your student login."

    elif "academic calendar" in user_input or "semester start" in user_input:
        return "The academic calendar is available on our website. The semester starts on July 10th."

    elif "syllabus" in user_input or "study material" in user_input:
        return "Syllabus and study materials can be downloaded from the LMS portal or collected from your department."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I’m Smart EduBot 🤖. How can I assist you today?"

    elif "thank" in user_input:
        return "You're welcome! 😊 Let me know if you need anything else."

    return None

# Main function to get chatbot response
def get_bot_response(user_input):
    # First try matching from the FAQ file
    response = search_faq(user_input)

    # If no FAQ match found, use rule-based logic
    if not response:
        response = rule_based_response(user_input)

    # If still no match, return fallback
    if not response:
        response = "I'm sorry, I couldn't find an answer for that. Please rephrase your question or contact support."

    return response
