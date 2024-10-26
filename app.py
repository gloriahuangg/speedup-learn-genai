import streamlit as st
from PyPDF2 import PdfReader
import docx
import io
import anthropic
import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Anthropic client with API key from .env
client = anthropic.Client(api_key=os.getenv('ANTHROPIC_API_KEY'))

def read_pdf(file) -> str:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def read_docx(file) -> str:
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def get_claude_response(prompt: str, content: str) -> Optional[str]:
    try:
        # Combine the prompt with the document content
        full_prompt = f"{prompt}\n\nDocument Content:\n{content}"
        
        # Get response from Claude
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        st.error(f"Error getting response from Claude: {str(e)}")
        return None

def analyze_document(text: str, analysis_type: str) -> Optional[str]:
    prompts = {
        "summary": """Please provide a comprehensive summary of the document. Include:
        1. Main topic and purpose
        2. Key arguments or findings
        3. Important conclusions
        4. Overall significance
        Make the summary clear and concise, focusing on the most important information.""",
        
        "key_points": """Extract and list the key points from the document. For each point:
        1. State the main idea clearly
        2. Provide any supporting evidence or examples
        3. Explain its significance in the context of the document
        Format the response as bullet points for easy reading.""",
        
        "study_questions": """Generate potential test questions that a teacher might ask students about this document. Include:
        1. Knowledge-based questions testing basic understanding
        2. Analysis questions requiring critical thinking
        3. Application questions connecting concepts to real-world scenarios
        4. Discussion questions encouraging deeper exploration
        For each question, provide a brief outline of what a good answer should include.""",
        
        "detailed_analysis": """Perform a detailed analysis of the document. Include:
        1. Structure and organization analysis
        2. Main arguments and evidence evaluation
        3. Methodology assessment (if applicable)
        4. Critical evaluation of strengths and weaknesses
        5. Connections to broader context or field
        6. Implications of the findings or arguments
        Make the analysis thorough but clear and well-organized."""
    }
    
    return get_claude_response(prompts[analysis_type], text)

def main():
    st.title("📚 Document Analysis Assistant to speed up your learning")
    st.write("Upload a document (PDF or DOCX) and get AI-powered analysis using Claude")
    
    # Check for API key
    if not os.getenv('ANTHROPIC_API_KEY'):
        st.error("Please set your ANTHROPIC_API_KEY environment variable")
        st.stop()
    
    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx'])
    
    if uploaded_file is not None:
        # Create a spinner while processing the file
        with st.spinner('Reading document...'):
            try:
                # Read the document based on its type
                if uploaded_file.type == "application/pdf":
                    text = read_pdf(uploaded_file)
                else:
                    text = read_docx(uploaded_file)
                
                # Store the document text in session state
                st.session_state['document_text'] = text
                st.success("Document successfully processed!")
            except Exception as e:
                st.error(f"Error processing document: {str(e)}")
                st.stop()
        
        # Create tabs for different types of analysis
        tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Key Points", "Study Questions", "Detailed Analysis"])
        
        with tab1:
            if st.button("Generate Summary", key="summary"):
                with st.spinner('Analyzing with Claude...'):
                    summary = analyze_document(st.session_state['document_text'], "summary")
                    if summary:
                        st.markdown(summary)
        
        with tab2:
            if st.button("Extract Key Points", key="key_points"):
                with st.spinner('Analyzing with Claude...'):
                    key_points = analyze_document(st.session_state['document_text'], "key_points")
                    if key_points:
                        st.markdown(key_points)
        
        with tab3:
            if st.button("Generate Study Questions", key="study_questions"):
                with st.spinner('Analyzing with Claude...'):
                    questions = analyze_document(st.session_state['document_text'], "study_questions")
                    if questions:
                        st.markdown(questions)
        
        with tab4:
            if st.button("Perform Detailed Analysis", key="detailed_analysis"):
                with st.spinner('Analyzing with Claude...'):
                    analysis = analyze_document(st.session_state['document_text'], "detailed_analysis")
                    if analysis:
                        st.markdown(analysis)
        
        # Add custom query section
        st.markdown("---")
        st.subheader("Ask Any Questions against the document")
        user_question = st.text_input("Enter your question about the document:")
        if user_question and st.button("Get Answer"):
            with st.spinner('Getting answer from Claude...'):
                prompt = f"""Please answer this question about the document: {user_question}
                Base your answer only on the information provided in the document."""
                answer = get_claude_response(prompt, st.session_state['document_text'])
                if answer:
                    st.markdown(answer)

if __name__ == "__main__":
    main()