# SVG Smuggler

`svg-smuggler.py` is a Python script that encodes a file into a Base64 string and embeds it into an SVG file. This SVG file contains a script that allows the user to download the original file when opened in a web browser.

## Prerequisites

- Python 3.x

## Usage

1. Ensure you have Python 3 installed on your system.
2. Run the script from the command line with the file you want to encode as an argument:

   ```bash
   python3 svg-smuggler.py <filename>
   ```

   Replace `<filename>` with the path to the file you want to encode.

3. The script will generate an `output.svg` file in the current directory.

## How It Works

- The script reads the specified file and encodes its contents into a Base64 string.
- It then creates an SVG file containing a script that can decode the Base64 string back into the original file.
- When the SVG is opened in a web browser, the script automatically triggers a download of the original file.

## Error Handling

- If no file is specified, the script will print an error message and exit.
- Any other exceptions encountered during execution will be caught and printed to the console.

