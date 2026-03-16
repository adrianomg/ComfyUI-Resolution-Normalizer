class ResolutionNormalizer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "value": ("INT", {
                    "default": 512,
                    "min": 360,
                    "max": 8192,
                    "step": 1
                }),
                "mode": (["min", "max", "sum"],),
            }
        }

    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "resolution")
    FUNCTION = "normalize"
    CATEGORY = "image/utils"

    def normalize(self, image, value, mode):

        # ComfyUI images are tensors: [batch, height, width, channels]
        height = image.shape[1]
        width = image.shape[2]

        if mode == "min":
            scale = value / min(width, height)
            new_width = round(width * scale)
            new_height = round(height * scale)

        elif mode == "max":
            scale = value / max(width, height)
            new_width = round(width * scale)
            new_height = round(height * scale)

        elif mode == "sum":
            new_width = round(value * width / (width + height))
            new_height = value - new_width

        else:
            new_width = width
            new_height = height

        resolution = f"{new_width} × {new_height}"

        return (int(new_width), int(new_height), resolution)


NODE_CLASS_MAPPINGS = {
    "ResolutionNormalizer": ResolutionNormalizer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionNormalizer": "Resolution Normalizer"
}