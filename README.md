# prompt

### Talk to Gemini from the CLI using the Vertex AI API. 

## Environment Variables  
`export VERTEX_PROJECT_ID="<PROJECT_ID>"`  
`export VERTEX_REGION="<REGION>"` 

### GCP Prerequisites  
Before running the script, ensure your Google Cloud environment is configured: 

1. **Active Project:** You must have a GCP Project with an active billing account.  
2. **Enable the API:** Enable the Vertex AI API for your project. You can do this in the web console or by running:  
   `gcloud services enable aiplatform.googleapis.com`  
3. **IAM Permissions:** Your Google account needs the **Vertex AI User** role to generate content.  
4. **gcloud:** https://docs.cloud.google.com/sdk/docs/install-sdk  

-------------------------------------------------------------------------- 

### Installation

1. Clone the repository and make the script executable:  
   `chmod +x prompt.py`  
2. Install the required Python package (using a virtual environment is recommended on newer Linux distributions):  
   `python3 -m venv venv`  
   `source venv/bin/activate`  
   `pip install vertexai` 
3. Authenicate with gcloud:  
   `gcloud auth application-default login`

------------------------------------------------------------------------- 

### usage: prompt.py [-h] [-f FILE] [-m MODEL] [prompt ...]  

example: `./prompt.py -f <file_path>`  
example: `./prompt.py -f <file_path> <input_text>`  
example: `./prompt.py -m <desired_model> -f <file_path> <input_text>`
