# Resolution Normalizer (ComfyUI Subgraph)

**Resolution Normalizer** is a small ComfyUI subgraph that rescales an
image resolution while **preserving the aspect ratio**, ensuring that
the **smallest side matches a chosen base resolution**.

This is useful when preparing images for Stable Diffusion pipelines that
expect a consistent base resolution while keeping the original
proportions.

------------------------------------------------------------------------

## Features

-   Preserves the original **aspect ratio**
-   Automatically **upscales or downscales**
-   Ensures the **smallest side equals the selected base resolution**
-   Simple drop-in subgraph for ComfyUI workflows

------------------------------------------------------------------------

## Inputs

  Input                 Type    Description
  --------------------- ------- --------------------------------------------------
  **image**             IMAGE   Image used to read the original width and height
  **Base resolution**   INT     Desired resolution for the smallest side

------------------------------------------------------------------------

## Outputs

  Output       Type   Description
  ------------ ------ -------------------
  **Width**    INT    Normalized width
  **Height**   INT    Normalized height

These outputs can be connected directly to nodes such as **Empty Latent
Image**, **Resize Image**, or other resolution-dependent nodes.

------------------------------------------------------------------------

## Installation

1. Download the `ResolutionNormalizer.json` file.

2. Copy the file into the following directory inside your ComfyUI installation: `ComfyUI/user/default/subgraphs/`

If the `subgraphs` directory does not exist, you can create it manually.

Example directory structure:

ComfyUI
├─ user
│  ├─ default
│  │  ├─ subgraphs
│  │  │  └─ ResolutionNormalizer.json

3. Restart ComfyUI.

The **Resolution Normalizer** subgraph should now be available in the node menu.

------------------------------------------------------------------------
## Usage

1. Add the **Resolution Normalizer** node to your workflow.
2. Connect an **image** input.
3. Set the **Base resolution** value.
4. Use the **Width** and **Height** outputs to drive nodes that require resolution inputs (for example, `Empty Latent Image`, `Resize Image`, etc.).

------------------------------------------------------------------------

## How It Works

The node calculates a scaling factor based on the smallest side of the
input image:

scale = base_resolution / min(width, height)

The new resolution is then computed proportionally:

new_width = width \* scale\
new_height = height \* scale

The values are rounded to integers to produce valid image dimensions.

------------------------------------------------------------------------

## Example

Original image:

1920 × 1080

Base resolution:

480

Result:

853 × 480

Aspect ratio is preserved while the smallest dimension becomes the
selected base resolution.

------------------------------------------------------------------------

## Use Cases

-   Preparing images for **Stable Diffusion**
-   Keeping consistent **latent resolution**
-   Normalizing images for **batch workflows**
-   Rescaling reference images while preserving proportions

------------------------------------------------------------------------

## Notes

-   The node may **upscale or downscale** depending on the input size.
-   Aspect ratio is always preserved.
-   The output values are **rounded to integers**.

------------------------------------------------------------------------

## License

Free to use and modify.
