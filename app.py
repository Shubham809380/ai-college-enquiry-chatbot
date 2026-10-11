
import streamlit as st
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="AI-Powered College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI-Powered College Enquiry Chatbot")
st.write(
    "Ask about admissions, courses, fees, scholarships, "
    "placements and hostel facilities."
)
st.caption(
    "Answers are based on the available FAQ dataset. "
    "Please verify important information with official college sources."
)


# --------------------------------------------------
# 2. CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# 3. LOAD FAQ DATA
# --------------------------------------------------
@st.cache_data
def load_faqs():
    data = pd.read_csv("faqs.csv").fillna("")

    required = {"question", "answer", "category"}

    if not required.issubset(data.columns):
        raise ValueError(
            "faqs.csv must contain question, answer and category columns."
        )

    for col in ["question", "answer", "category"]:
        data[col] = data[col].astype(str).str.strip()

    data = data[
        (data["question"] != "") &
        (data["answer"] != "")
    ].reset_index(drop=True)

    if data.empty:
        raise ValueError("No valid FAQ entries found.")

    # Normalize categories
    data["category"] = data["category"].str.lower()

    return data


try:
    df = load_faqs()

except FileNotFoundError:
    st.error("faqs.csv nahi mili. app.py ke same folder mein rakho.")
    st.stop()

except pd.errors.EmptyDataError:
    st.error("faqs.csv is empty.")
    st.stop()

except (ValueError, pd.errors.ParserError) as error:
    st.error(f"Dataset error: {error}")
    st.stop()

except UnicodeDecodeError:
    st.error("CSV encoding error. Save the file using UTF-8.")
    st.stop()


# --------------------------------------------------
# 4. PREPARE FAQ MATCHING
# --------------------------------------------------
try:
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        sublinear_tf=True
    )

    faq_matrix = vectorizer.fit_transform(df["question"])

except ValueError:
    st.error("FAQ questions contain no usable text.")
    st.stop()


# --------------------------------------------------
# 5. CATEGORY KEYWORDS
# --------------------------------------------------
CATEGORY_KEYWORDS = {
    "scholarships": [
        "scholarship", "scholarships", "financial aid",
        "fee waiver", "education grant"
    ],
    "courses": [
        "course", "courses", "degree", "program",
        "programs", "curriculum", "branch", "branches"
    ],
    "placements": [
        "placement", "placements", "job", "jobs",
        "recruiter", "recruiters", "company", "companies",
        "placement cell", "campus recruitment"
    ],
    "admission": [
        "admission", "admissions", "apply for admission",
        "application form", "enrolment", "enrollment"
    ],
    "fees": [
        "fee", "fees", "tuition", "payment", "cost"
    ],
    "hostel": [
        "hostel", "accommodation", "dormitory", "mess"
    ]
}


def detect_category(query):
    """Return a category when a clear topic keyword is present."""
    text = query.lower()
    padded_text = f" {text} "

    matches = []

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            # Allow multi-word keyword matches and simple word boundaries
            if keyword in text:
                matches.append((category, len(keyword)))

    if not matches:
        return None

    # Prefer the most specific/longest keyword match
    matches.sort(key=lambda item: item[1], reverse=True)
    return matches[0][0]


# --------------------------------------------------
# 6. ANSWER MATCHING FUNCTION
# --------------------------------------------------
def get_answer(query):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, faq_matrix)[0]

    # Limit matching to the detected category when possible
    detected = detect_category(query)

    eligible = list(range(len(df)))

    if detected:
        category_rows = [
            i for i, category in enumerate(df["category"])
            if detected in category
        ]

        if category_rows:
            eligible = category_rows

    best_index = max(eligible, key=lambda i: scores[i])
    best_score = float(scores[best_index])

    # Conservative threshold: do not answer weak matches
    if best_score >= 0.30:
        return str(df.loc[best_index, "answer"])

    return (
        "Sorry, I could not find a verified answer. "
        "Please contact the relevant college office."
    )


# --------------------------------------------------
# 7. SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write("FAQ-based college enquiry assistant.")
    st.write(f"**Available FAQs:** {len(df)}")

    categories = sorted(
        category for category in df["category"].unique()
        if category
    )

    st.write("**FAQ categories:**")
    for category in categories:
        st.write(f"- {category.title()}")

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# --------------------------------------------------
# 8. DISPLAY CONVERSATION
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# 9. HANDLE NEW QUESTION
# --------------------------------------------------
query = st.chat_input("Ask your college question...")

if query and query.strip():
    clean_query = re.sub(r"\s+", " ", query).strip()

    st.session_state.messages.append({
        "role": "user",
        "content": clean_query
    })

    with st.chat_message("user"):
        st.write(clean_query)

    answer = get_answer(clean_query)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)
