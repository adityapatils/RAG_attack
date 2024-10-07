
# RAG-based Resume Query Application

This project is a **Retrieval-Augmented Generation (RAG)** system designed to query IT resumes from a PDF document. It uses **FastAPI** for backend services and **Streamlit** for an interactive front-end interface.

---

## Project Structure

```
project/
│
├── app.py                     # Streamlit application for querying IT resumes.
├── fastapi_app.py             # FastAPI application providing the API for querying resumes.
├── basics_RAG_pdf.ipynb        # Jupyter Notebook demonstrating RAG setup with PDFs.
├── IT_resumes.pdf             # Sample PDF file containing IT resumes.
├── requirements.txt           # List of dependencies for the project.
├── env.txt                    # Environment variables like API keys.
└── README.md                  # Project documentation.
```

---

## File Descriptions

- **app.py**:  
  The main front-end built using Streamlit that provides a user interface for querying the resumes.
  
- **fastapi_app.py**:  
  Backend service created with FastAPI that offers an API to send queries and get answers from the RAG model.
  
- **basics_RAG_pdf.ipynb**:  
  Jupyter Notebook demonstrating the RAG system, including PDF loading, text splitting, embedding creation, and retrieval.

- **IT_resumes.pdf**:  
  A sample PDF document used to test the system's query functionality.
  
- **requirements.txt**:  
  Contains all the necessary dependencies required for this project.
  
- **env.txt**:  
  A file that holds environment variables such as `GOOGLE_API_KEY`, necessary for accessing Google Generative AI models.

- **README.md**:  
  Documentation explaining the project, setup instructions, and usage.

---

## Environment Setup

1. **Create a virtual environment**:
   ```bash
   conda create -n env_langchain1 python=3.10  
   conda activate env_langchain1
   ```

2. **Upgrade pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Install project dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Applications

### 1. Running the Streamlit App

To launch the Streamlit app, which provides an interactive interface for querying resumes:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the app in your default browser.

---

### 2. Running the FastAPI Application

To run the FastAPI backend, execute:

```bash
python fastapi_app.py
```

By default, the FastAPI application will run at `http://127.0.0.1:8000`. You can access the interactive API docs at:

- [Swagger UI (API Documentation)](http://127.0.0.1:8000/docs)

---

## Additional Information

### API Documentation
The FastAPI app provides a Swagger UI at `http://127.0.0.1:8000/docs`. You can interactively test the endpoints here.

### Testing
You can test API calls using:
- **cURL**
- **Postman**
- Directly through the **Swagger UI**

### Environment Variables
Ensure that you include the necessary API keys (e.g., `GOOGLE_API_KEY`) in the environment file (`env.txt`) for the generative AI features to function properly.

---

## Third-Party Libraries

The project uses the following third-party libraries:

- **LangChain**: For building language models and text retrieval.
- **Streamlit**: Provides the interactive UI for querying the resumes.
- **FastAPI**: Backend framework for handling API requests.
- **Google Generative AI Embeddings**: Used to embed documents for query processing.
- **Chroma**: For vector storage and retrieval.
- **PyPDF**: For loading and parsing PDF documents.

For the complete list of dependencies, please check the `requirements.txt` file.

---

## How to Use

1. Set up the environment by following the **Environment Setup** instructions.
2. Run the **FastAPI** backend (`fastapi_app.py`).
3. Run the **Streamlit** app (`app.py`).
4. Use the Streamlit UI to query resumes from the sample PDF (`IT_resumes.pdf`).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## Contact

For any questions or feedback, feel free to reach out!
