from PIL import Image
import os

# Define paths
layers_path = "E:/NFTTest3/layers"
output_path = "E:/NFTTest3/output"

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Get all layer folders in the correct order (adjust order as needed)
layer_folders = [f for f in os.listdir(layers_path) if os.path.isdir(os.path.join(layers_path, f))]
layer_folders.sort()  # Ensure layers are processed in alphabetical order or customize as needed

# Load all possible images from each layer
layers = {}
for layer in layer_folders:
    layer_path = os.path.join(layers_path, layer)
    layers[layer] = [os.path.join(layer_path, f) for f in os.listdir(layer_path) if f.endswith(".png")]

# Initialize global NFT count
nft_count = 0

# Generate NFTs
for background in layers.get("background", []):
    base_image = Image.open(background).convert("RGBA").resize((600, 600))

    # Loop through combinations of other layers
    def generate_combinations(current_image, current_layers):
        global nft_count

        if not current_layers:
            # Save the generated NFT
            output_file = os.path.join(output_path, f"nft_{nft_count}.png")
            current_image.save(output_file, "PNG")
            nft_count += 1
            return

        # Process the next layer
        next_layer_name, *remaining_layers = current_layers
        for item in layers[next_layer_name]:
            layer_image = Image.open(item).convert("RGBA").resize((600, 600))
            combined_image = Image.alpha_composite(current_image, layer_image)
            generate_combinations(combined_image, remaining_layers)

    # Start generating combinations for the current background
    remaining_layer_names = [layer for layer in layer_folders if layer != "background"]
    generate_combinations(base_image, remaining_layer_names)

print(f"{nft_count} NFTs generated and saved in: {output_path}")
