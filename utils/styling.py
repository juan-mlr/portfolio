from collections.abc import Iterable


def image_column_widths(
        sizes: Iterable[tuple[int]],
        target_height: int
    ) -> list[float]:
    aspect_ratios = [size[0] / size[1] for size in sizes]
    return [target_height * ratio for ratio in aspect_ratios]
