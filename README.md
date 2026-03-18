# Resolution Normalizer (ComfyUI Node)

**Resolution Normalizer** is a utility node for ComfyUI that rescales image resolutions while preserving the aspect ratio.

The node supports multiple normalization strategies, allowing you to normalize an image resolution by its **minimum side**, **maximum side**, or **the sum of width and height**.

This makes it useful for preparing images for Stable Diffusion pipelines, resizing reference images, or normalizing resolutions across workflows.

<img src="https://github.com/adrianomg/ComfyUI-Resolution-Normalizer/blob/main/images/node.png?raw=true" width=25% height=25%>

## Example Workflow
<img src="https://github.com/adrianomg/ComfyUI-Resolution-Normalizer/blob/main/images/example_workflow.png?raw=true">

---

## Features

- Preserve the original **aspect ratio**
- Normalize resolution using different strategies
- Automatically **upscale or downscale**
- Output the calculated **width and height**
- Display the resulting resolution as a formatted string

---

## Installation

1. Clone or download this repository.

2. Copy the repository into the ComfyUI `custom_nodes` directory:

3. Restart ComfyUI.

The **Resolution Normalizer** node will appear in the node menu.

---

## Node Inputs

| Input | Type | Description |
|------|------|-------------|
| image | IMAGE | Image used to determine the original resolution |
| value | INT | Target normalization value |
| mode | ENUM | Normalization mode (`min`, `max`, or `sum`) |

---

## Node Outputs

| Output | Type | Description |
|------|------|-------------|
| width | INT | Calculated width |
| height | INT | Calculated height |
| resolution | STRING | Formatted resolution string (e.g. `1280 × 720`) |

---

## Normalization Modes

### Min Mode

Ensures the **smallest side** of the image equals the target value.

Example:

Input image: 1920 × 1080
Target value: 480
Result: 853 × 480

---

### Max Mode

Ensures the **largest side** of the image equals the target value.

Example:

Input image: 1920 × 1080
Target value: 1024
Result: 1024 × 576

---

### Sum Mode

Ensures the **sum of width and height** equals the target value.

Example:

Input image: 1920 × 1080
Target value: 2000
Result: 1280 × 720

---

## Example Use Cases

### Preparing images for Stable Diffusion

Normalize images so the smallest side matches a base resolution:

mode: min
value: 768

---

### Limiting maximum image size

Prevent images from exceeding a given resolution:

mode: max
value: 1024

---

### Normalizing images across a dataset

Ensure image resolution scale consistently based on their total dimensions.
This is useful to keep the computational cost constant.

mode: sum
value: 2000

---

## License

This project is released under the MIT License.
