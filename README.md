# prompt

dependencies: vertexai 

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