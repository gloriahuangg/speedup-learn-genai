# Document Analysis Assistant to speed up learning📚

A Streamlit web application that uses Claude AI to analyze PDF and DOCX documents. The application provides intelligent document analysis including summaries, key points extraction, study questions generation, and detailed analysis.

## Features 🌟

- **Document Upload**: Support for PDF and DOCX files
- **Multiple Analysis Types**:
  - Comprehensive document summaries
  - Key points extraction
  - Study questions generation with answer guidelines
  - Detailed document analysis
- **Custom Questions**: Ask specific questions about the document content
- **AI-Powered**: Utilizes Claude AI (Anthropic) for intelligent analysis
- **User-Friendly Interface**: Clean and intuitive Streamlit interface
- **Real-time Processing**: Instant document processing and analysis

## Prerequisites 📋

Before running the application, make sure you have Python 3.7+ installed on your system. tested with python 3.11.

## Installation 🛠️

1. Clone the repository:
```bash
git clone <repository-url>
cd document-analysis-assistant
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Anthropic API key:
```plaintext
ANTHROPIC_API_KEY=your-api-key-here
```

## Usage 🚀

1. Start the Streamlit application:
```bash
streamlit run doc_analyzer.py
```

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Use the application:
   - Upload a PDF or DOCX document using the file uploader
   - Choose from various analysis options in the tabs
   - Get AI-powered analysis of your document
   - Ask custom questions about the document content

## Project Structure 📁

```
document-analysis-assistant/
├── doc_analyzer.py        # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this file)
└── README.md             # Project documentation
```

## Dependencies 📦

- `streamlit`: Web application framework
- `PyPDF2`: PDF file processing
- `python-docx`: DOCX file processing
- `anthropic`: Claude AI API client
- `python-dotenv`: Environment variable management

## Environment Variables 🔑

The application requires the following environment variable in the `.env` file:

- `ANTHROPIC_API_KEY`: Your Anthropic API key for accessing Claude AI

## API Usage 📊

The application uses the Claude 3 Sonnet model from Anthropic with the following configuration:
- Max tokens: 4096
- Temperature: 0.7
- Model: claude-3-sonnet-20240229

## Error Handling ⚠️

The application includes error handling for:
- Missing API key
- Document processing errors
- API response errors
- Invalid file types

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Anthropic for providing the Claude AI API
- Streamlit for the excellent web application framework
- The open-source community for various dependencies

## Support 💬

For support and questions, please open an issue in the repository or contact the maintainers.

## TODO 📝

Future improvements could include:
- [ ] Support for more document formats
- [ ] Batch processing of multiple documents
- [ ] Export functionality for analysis results
- [ ] Additional analysis types
- [ ] Customizable AI parameters
- [ ] Document comparison features