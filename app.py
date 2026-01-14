import streamlit as st
import chromadb
import google.generativeai as genai
import os

# 1. SETUP THE INTERFACE
st.set_page_config(page_title="SOP Analyzer", page_icon="SS")
st.title(" University SOP Analyzer ")
st.write("Compare your draft against successful essays")

# 2. CONNECT TO GEMINI 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. CONNECT TO DATABASE
db_path = r"C:\Users\nsaha\OneDrive\Desktop\SOP_Analyzer\essay_db"
chroma_client = chromadb.PersistentClient(path=db_path)
collection = chroma_client.get_collection(name="accepted_essays")

# 4. USER INPUTS
target_school = st.selectbox("Which school are you applying to?", ["Harvard", "Johns Hopkins", "Connecticut"])
user_draft = st.text_area("Paste your draft here:", height=400)

if st.button("Analyze My Draft"):
    if user_draft:
        with st.spinner(f'Searching {target_school} database...'):
            # Retrieval: Find the top 2 matching essays from your database
            results = collection.query(
                query_texts=[user_draft], 
                n_results=2,
                where={"school": target_school}
            )
            context = results['documents'][0]

            # 5. THE PROMPT 
            prompt = f"""
            You are an expert Admissions Dean for {target_school}. 
            Below are two real essays that were previously ACCEPTED to this school:
            ---
            {context}
            ---
            Now, here is a student's DRAFT:
            {user_draft}

            TASK:
            1. Rate the draft's 'Institutional Fit' out of 100.
            2. Identify 2 specific things the successful essays did that this draft is missing.
            3. Give 3 actionable steps to improve the tone and content.
            Dont say As an Admissions Dean for Johns Hopkins, I evaluate essays for intellectual curiosity, personal growth, resilience, impact, and a demonstrated ability to contribute to our vibrant community.

It's an interesting exercise to review this particular draft, as it is, in fact, one of the previously accepted essays you provided! This immediately tells me its inherent strength and appeal to our admissions committee.
just say something like here is the analysis           """

            # 6. CALL GEMINI
            response = model.generate_content(prompt)
            
            st.success("Analysis Complete!")
            st.subheader("Admissions Officer Report")
            st.write(response.text)
    else:
        st.warning("Please paste a draft first.")