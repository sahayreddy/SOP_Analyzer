🎓 AI-Powered University SOP Analyzer:
A Retrieval-Augmented Generation (RAG) tool for institution-specific essay analysis.

🌟 Project HighlightsInstitution-Specific Critique:
 1.Unlike general AI, this tool compares student drafts against a private database of real successful essays.
 2.Advanced RAG Architecture: Implements a full Retrieval-Augmented Generation pipeline using vector embeddings and semantic search.
 3.Interactive Dashboard: A sleek web interface with a real-time "Institutional Fit" gauge.
 
 🚀 The Problem & Motivation:
 Standard AI tools give generic writing advice. However, every university (Harvard vs. Johns Hopkins) has a distinct "vibe" and set of values they look for in a Statement of Purpose (SOP). I built this project to bridge that gap, providing students with a tool that uses actual successful examples as a benchmark for feedback.
 
 🛠️ Tech StackComponentTechnologyRoleLanguagePython 3.13Core application logic and data processing.AI BrainGoogle Gemini 2.5 FlashAdvanced LLM for generating "Gap Analysis" reports.Vector DBChromaDBSemantic memory for indexing and retrieving accepted essays.Web UIStreamlitInteractive frontend for user input and results display.VisualizationPlotlyDynamic gauge charts for fit-score visualization.
 
 🧠 How It Works (The RAG Pipeline):
 
  1.Data Ingestion: Successful essays are cleaned, chunked, and converted into mathematical vectors (embeddings).
  
  2.Semantic Retrieval: When a student pastes a draft, the system searches the database for the 2 most similar successful essays from the same university.
  
  3.Context Injection: These examples are injected into a specialized "Admissions Dean" prompt.Analysis: Gemini 2.5 identifies precisely what is missing in the student's draft compared to the winners.

  In the files i have uploaded there is a data file where in there are all the accepted essays that i have used for each university and then in the codes folder there is a app.py file which is the main code on whuch this whole application works and there is a sop_analyze file as well as a read_file which were preliminary codes written to check if this code would run before making a whole application out of it 
