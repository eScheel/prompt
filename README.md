# prompt

dependencies: gcloud, vertexai 

export VERTEX_PROJECT_ID="<PROJECT_ID>"  
export VERTEX_REGION="<REGION_ID>" 

gcloud auth application-default login 

### GCP Prerequisites  
Before running the script, ensure your Google Cloud environment is configured: 

1. **Active Project:** You must have a GCP Project with an active billing account.  
2. **Enable the API:** Enable the Vertex AI API for your project. You can do this in the web console or by running:  
   `gcloud services enable aiplatform.googleapis.com`  
3. **IAM Permissions:** Your Google account needs the **Vertex AI User** role to generate content.  

-------------------------------------------------------------------------- 

usage: prompt.py [-h] [-f FILE] [-m MODEL] [prompt ...] 

Talk to Gemini from the CLI. 

positional arguments:
  prompt             input text 

options:  
  -h, --help         show this help message and exit  
  -f, --file FILE    Path to a file (text, image, pdf, etc.)  
  -m, --model MODEL  The Gemini model to use (default: gemini-2.5-pro)  

-------------------------------------------------------------------------- 

example: ./prompt.py -f <file_path>  
example: ./prompt.py -f <file_path> <input_text>  
example: ./prompt.py -m <model> -f <file_path> <input_text>
