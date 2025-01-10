from PIL import Image
import os

# Define paths
layers_path = "E:/NFTTest3/layers"
background_path = os.path.join(layers_path, "background", "body.png")
crown_path = os.path.join(layers_path, "crown")
output_path = "E:/NFTTest3/output"

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Load the body image
body = Image.open(background_path).convert("RGBA")
body = body.resize((600, 600))

# List all crowns
crown_files = [f for f in os.listdir(crown_path) if f.endswith(".png")]

# Generate NFTs
for crown_file in crown_files:
    crown = Image.open(os.path.join(crown_path, crown_file)).convert("RGBA")
    crown = crown.resize((600, 600))

    # Composite the images
    combined = Image.alpha_composite(body, crown)

    # Save the output
    output_file = os.path.join(output_path, f"nft_{os.path.splitext(crown_file)[0]}.png")
    combined.save(output_file, "PNG")

print(f"NFTs generated and saved in: {output_path}")
