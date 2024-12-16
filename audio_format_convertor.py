import os
from pydub import AudioSegment

# Create 'In' directory if it doesn't exist
if not os.path.exists("In"):
    os.makedirs("In")

# Process all files in OtherFormat directory
for filename in os.listdir("OtherFormat"):
    if filename.endswith(('.m4a', '.mp3', '.ogg', '.wav')):  # Add more formats if needed
        # Get the file name without extension
        name_without_ext = os.path.splitext(filename)[0]
        
        # Convert and save to In directory
        input_path = os.path.join("OtherFormat", filename)
        output_path = os.path.join("In", name_without_ext + ".wav")
        
        # Convert the file
        AudioSegment.from_file(input_path).export(output_path, format="wav")
        print(f"Converted {filename} to {output_path}")

