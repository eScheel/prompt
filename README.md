# prompt

### Talk to Gemini from the CLI using the Vertex AI API. 

-------------------------------------------------------------------------- 

### GCP Prerequisites  
Before running the script, ensure your Google Cloud environment is configured: 

1. **Active Project:** You must have a GCP Project with an active billing account.  
2. **Enable the API:** Enable the Vertex AI API for your project. You can do this in the web console or by running:  
   `gcloud services enable aiplatform.googleapis.com`  
3. **IAM Permissions:** Your Google account needs the **Vertex AI User** role to generate content.  
4. **Download and Install gcloud:** https://docs.cloud.google.com/sdk/docs/install-sdk  

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

**Environment Variables**  
`export VERTEX_PROJECT_ID="<PROJECT_ID>"`  
`export VERTEX_REGION="<REGION>"` 

------------------------------------------------------------------------- 

### usage: prompt.py [-h] [-f FILE] [-m MODEL] [prompt ...]  

example: `./prompt.py <input_text>`  
example: `./prompt.py -f <file_path>`  
example: `./prompt.py -f <file_path> <input_text>`  
example: `./prompt.py -m <model_id> -f <file_path> <input_text>` 

------------------------------------------------------------------------ 

**INFO** 

You may run into the following errors when invoking the script:  
`env: ‘python3\r’: No such file or directory`  
`env: use -[v]S to pass options in shebang lines`  
This is because of how Windows handles Line feeds different from UNIX/Linux. 

To fix this you will need to run a program against the script such as `dos2unix` which should be easily downloadable via built-in package manager.
