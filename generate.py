# generate.py
from PIL import Image
import os
import random

# Define paths
layers_path = "E:/NFTTest3/layers"
output_path = "E:/NFTTest3/output"

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Load traits and groups
group_1 = ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue"]
group_2 = ["original", "white"]

# Define layer folders
layer_folders = ["background", "chain", "earing", "crown", "sash", "band"]

# Load all possible images from each layer
layers = {}
for layer in layer_folders:
    layer_path = os.path.join(layers_path, layer)
    layers[layer] = {
        "group_1": [os.path.join(layer_path, f) for f in os.listdir(layer_path) if any(color in f for color in group_1)],
        "group_2": [os.path.join(layer_path, f) for f in os.listdir(layer_path) if any(color in f for color in group_2)]
    }
    print(f"{layer} - Group 1: {len(layers[layer]['group_1'])}, Group 2: {len(layers[layer]['group_2'])}")

# Generate NFTs
nft_count = 0
max_nfts = 500
selected_rarity_indices = set(random.sample(range(max_nfts), 100))

background_images = layers["background"]["group_1"]
if background_images:
    for _ in range(max_nfts):
        background = random.choice(background_images)
        base_image = Image.open(background).convert("RGBA").resize((600, 600))

        def generate_combinations(current_image, current_layers, index):
            global nft_count
            if nft_count >= max_nfts:
                return

            if not current_layers:
                output_file = os.path.join(output_path, f"nft_{nft_count}.png")
                current_image.save(output_file, "PNG")
                nft_count += 1
                return

            next_layer_name, *remaining_layers = current_layers

            for group in ["group_1", "group_2"]:
                probability = 0.95 if (index in selected_rarity_indices and group == "group_1") else 0.05
                if random.random() <= probability:
                    for item in layers[next_layer_name][group]:
                        if nft_count >= max_nfts:
                            return
                        layer_image = Image.open(item).convert("RGBA").resize((600, 600))
                        combined_image = Image.alpha_composite(current_image, layer_image)
                        generate_combinations(combined_image, remaining_layers, index)

        remaining_layer_names = [layer for layer in layer_folders if layer != "background"]
        generate_combinations(base_image, remaining_layer_names, nft_count)

print(f"{nft_count} NFTs generated and saved in: {output_path}")