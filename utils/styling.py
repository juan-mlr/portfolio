import streamlit as st

from collections.abc import Iterable
from PIL.JpegImagePlugin import JpegImageFile


def image_column_widths(
        sizes: Iterable[tuple[int]],
        target_height: int
    ) -> list[float]:
    aspect_ratios = [size[0] / size[1] for size in sizes]
    return [target_height * ratio for ratio in aspect_ratios]

def st_image_row(
        images: Iterable[JpegImageFile],
        captions: Iterable[str],
        target_height: int
    ) -> None:
    sizes = [im.size for im in images]
    widths = image_column_widths(sizes, target_height)
    cols = st.columns(widths)
    for col, image, caption in zip(cols, images, captions):
        with col:
            st.image(image, caption)
