#!/usr/bin/env python3

import os
import sys
import argparse
import mimetypes
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

PROJECT_ID = os.environ.get("VERTEX_PROJECT_ID")
REGION = os.environ.get("VERTEX_REGION")

# Entry Point.
if __name__ == "__main__":   
    # ---------------------------------------------------------
    # 1. SETTING UP COMMAND LINE ARGUMENTS AND HELP
    # ---------------------------------------------------------
    parser = argparse.ArgumentParser(description="Talk to Gemini from the CLI.")
    parser.add_argument("prompt", nargs="*", help="input text")
    parser.add_argument("-f", "--file", type=str, help="Path to a file (text, image, pdf, etc.)")
    parser.add_argument("-m", "--model", type=str, default="gemini-2.5-pro", help="The Gemini model to use (default: gemini-2.5-pro)")

    # This actually parses what the user typed and stores it in the 'args' object.
    args = parser.parse_args()

    # Take that list of words stored in args.prompt and glue them back together into a single string, separated by spaces.
    final_prompt = " ".join(args.prompt)
    
    # Initialize file_part to None so we have a predictable starting state.
    file_part = None

    # ---------------------------------------------------------
    # 2. FILE HANDLING & MIME TYPES
    # ---------------------------------------------------------
    # Check if the user actually used the -f flag
    if args.file:
        try:
            # guess_type returns a tuple: (type, encoding). We only care about the type,
            # so we use an underscore '_' to throw away the encoding part.
            mime_type, _ = mimetypes.guess_type(args.file)
            
            # If the file has no extension or a weird one, default to plain text
            if mime_type is None:
                mime_type = "text/plain"

            # Check if the MIME type indicates a text-based file (text/plain, text/csv, text/html, etc.)
            if mime_type.startswith("text/"):
                
                # 'with open' automatically handles closing the file descriptor when done.
                # 'r' means read mode, treating the contents as a standard decoded string.
                with open(args.file, "r", encoding="utf-8") as f:
                    file_content = f.read()
                
                # Append the text file's contents directly to the user's prompt
                final_prompt += f"\n\n--- Content of {args.file} ---\n{file_content}"
            
            # If it's NOT a text file (e.g., image/jpeg, application/pdf)
            else:
                # 'rb' means read-binary. We read the raw byte stream into memory.
                with open(args.file, "rb") as f:
                    file_bytes = f.read()
                
                # Google's API expects binary data to be packaged inside a 'Part' object.
                # We give it the raw bytes and tell it what MIME type those bytes represent.
                file_part = Part.from_data(data=file_bytes, mime_type=mime_type)
                
        # Catch errors if the user types a file name that doesn't exist
        except FileNotFoundError:
            sys.exit(f"Error: Could not find the file '{args.file}'")
        # Catch any other weird permissions or reading errors
        except Exception as e:
            sys.exit(f"Error reading file: {e}")

    # ---------------------------------------------------------
    # 3. SAFETY CHECKS
    # ---------------------------------------------------------
    # If final_prompt is completely empty...
    if not final_prompt.strip():
        # ...but we provided a binary file (like an image)...
        if file_part:
            # Give the model a generic instruction so it doesn't crash from an empty text prompt
            final_prompt = "Please analyze and describe this file."
        else:
            # If provided NO prompt and NO file, print the help menu and exit.
            parser.print_help()
            sys.exit()

    # ---------------------------------------------------------
    # 4. API COMMUNICATION & STREAMING
    # ---------------------------------------------------------
    # Dynamically inject the chosen model name into the print statement
    print(f"Contacting the {args.model} model and generating a response ...")
    print("============================================")
    
    # Authenticate and set parameters and select a model.
    vertexai.init(project=PROJECT_ID, location=REGION)
    
    # Pass the argument dynamically instead of hardcoding it
    model = GenerativeModel(args.model)
    
    try:
        # Finalize the content and generate the responses.
        content = [file_part, final_prompt] if file_part else final_prompt  
        responses = model.generate_content(content, stream=True)
        
        # Loop over the chunks arriving over the network.
        for chunk in responses:
            print(chunk.text, end="", flush=True)
        print() # Prints a newline after all response chunks.
        
    # Catch API errors (like quota limits, network drops, or safety blocks)
    except Exception as e:
        print(f"\nAn error occurred while generating the response: {e}")
        
    sys.exit("============================================")