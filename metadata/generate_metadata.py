import os
import json

# Paths
output_images_path = "E:/NFTTest3/output"
metadata_output_path = "E:/NFTTest3/metadata"

# Ensure the metadata directory exists
os.makedirs(metadata_output_path, exist_ok=True)

# Example traits and values
traits = {
    "Background": ["Blue", "Green", "Red"],
    "Band": ["Gold", "Silver", "Black"],
    "Chain": ["Diamond", "Gold", "Silver"],
    "Crown": ["Ruby", "Emerald", "Sapphire"],
    "Earring": ["Pearl", "Diamond", "None"],
    "Sash": ["Silk Red", "Silk Blue", "Velvet Black"]
}

# Generate metadata for each NFT
nft_files = [f for f in os.listdir(output_images_path) if f.endswith(".png")]

for nft_file in nft_files:
    nft_id = nft_file.split(".")[0]  # Extract NFT ID from filename

    # Generate metadata
    metadata = {
        "name": f"NFT #{nft_id}",
        "description": "This is a unique NFT from my collection.",
        "image": f"https://example.com/nft/{nft_file}",  # Replace with actual image URL
        "attributes": []
    }

    # Add random traits (or logic-based selection)
    for trait_type, values in traits.items():
        selected_value = values[0]  # Adjust to use random.choice(values) if you want random
        metadata["attributes"].append({
            "trait_type": trait_type,
            "value": selected_value
        })

    # Save metadata to JSON file
    metadata_file_path = os.path.join(metadata_output_path, f"{nft_id}.json")
    with open(metadata_file_path, "w") as metadata_file:
        json.dump(metadata, metadata_file, indent=4)

print(f"Metadata for {len(nft_files)} NFTs saved in: {metadata_output_path}")
