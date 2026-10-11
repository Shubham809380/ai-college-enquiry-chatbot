# 🎓 AI-Powered College Enquiry Chatbot

## 📌 Project Overview

The AI-Powered College Enquiry Chatbot is a web-based application developed using Python and Streamlit. It helps students and parents find answers to common college-related questions about admissions, courses, fees, scholarships, placements, and hostel facilities.

The chatbot uses **TF-IDF vectorization and cosine similarity** to compare user questions with questions stored in an FAQ dataset. It returns the answer associated with the most relevant FAQ when the similarity score meets the configured threshold. If a suitable answer is not found, it displays a safe fallback message.

## 🎯 Objectives

- Automate responses to frequently asked college enquiry questions.
- Provide a simple and user-friendly chatbot interface.
- Match questions with relevant FAQ entries.
- Avoid unsupported answers by using a fallback response.
- Make college information easier to access.

## ✨ Features

- 💬 Interactive chat interface.
- 🎓 College admission-related enquiries.
- 📚 Course and curriculum enquiries.
- 💰 Fee and scholarship enquiries.
- 🏢 Placement-related enquiries.
- 🏠 Hostel-related enquiries.
- 🔎 FAQ matching using TF-IDF and cosine similarity.
- 🛡️ Fallback response for unsupported questions.
- 🗂️ Chat history during the current Streamlit session.
- 🗑️ Clear Chat History option.
- 📄 CSV-based FAQ dataset.
- ⚠️ Basic dataset validation and error handling.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | FAQ dataset loading and processing |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| CSV | FAQ data storage |
| Git and GitHub | Version control and source code hosting |

## ⚙️ How It Works

1. The user enters a question in the chatbot.
2. The application preprocesses the FAQ dataset.
3. TF-IDF converts FAQ questions into numerical text vectors.
4. Cosine similarity compares the user's question with the FAQ questions.
5. The application prioritizes the relevant category when a category is detected.
6. If the best similarity score meets the configured threshold, the corresponding FAQ answer is displayed.
7. Otherwise, the chatbot displays a fallback message directing the user to the relevant college office.

## 📁 Project Structure

```text
AI-College-Enquiry-Chatbot/
│
├── app.py
├── faqs.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Visual Studio Code
- pip package manager

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd AI-College-Enquiry-Chatbot
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```powershell
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser. If it does not open automatically, use the local URL shown in the terminal, usually `http://localhost:8501`.

## 📋 Requirements

The `requirements.txt` file should contain:

```text
streamlit
pandas
scikit-learn
```

## 🧪 Testing

The following test cases were checked during development:

| Test Case | Expected Result | Status |
|---|---|---|
| Admission enquiry | Relevant admission answer | Passed |
| Scholarship availability | Relevant scholarship answer | Passed |
| Course enquiry | Relevant course answer | Passed |
| Scholarship application | Relevant scholarship answer | Passed |
| Placement information | Relevant placement answer | Passed |
| Unrelated question, such as a joke request | Safe fallback response | Passed |

These results reflect the test questions checked during development. Additional testing is required for spelling errors, ambiguous questions, missing files, and other edge cases.

## 🔒 Limitations

- The chatbot depends on the quality and completeness of the FAQ dataset.
- TF-IDF matching does not understand meaning as deeply as modern language models.
- Similarity-based matching can occasionally select an incorrect answer.
- College information must be verified and updated by an authorized person.
- The chatbot does not automatically retrieve live information from college websites.
- The fallback message does not replace contacting the relevant college office.

## 🚀 Future Enhancements

- Multilingual support for English, Hindi, and Odia.
- Voice-based questions and answers.
- Semantic search using sentence embeddings.
- An admin dashboard for updating FAQs.
- Integration with verified college information sources.
- Improved analytics and chatbot evaluation.
- Deployment on a public hosting platform.

## 📌 Conclusion

The AI-Powered College Enquiry Chatbot demonstrates how text processing and similarity-based information retrieval can automate common college enquiries. It provides a simple interface for accessing FAQ-based information while using a fallback response when a sufficiently relevant answer is not available.

## 👨‍💻 Author

**Name:** Shubham Patra

**Project:** AI-Powered College Enquiry Chatbot

**Institution:** Gandhi Institute of Excellent Technocrats

## 📄 Disclaimer

This project is an educational demonstration. The FAQ answers should be verified against official college information before being used for real admission, fee, scholarship, or placement decisions.