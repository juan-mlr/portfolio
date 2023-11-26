from PIL import Image
from requests import get

from PIL.JpegImagePlugin import JpegImageFile


# TODO: ~ from streamlit.runtime import _get_websocket_headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

def image_from_url(url: str) -> JpegImageFile:
    return Image.open(
        get(
            url,
            headers=headers,
            stream=True
        ).raw
    )
