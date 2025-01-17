# generate_metadata.py
import os
import json
import random

# Paths
output_images_path = "E:/NFTTest3/output"
metadata_output_path = "E:/NFTTest3/metadata"

os.makedirs(metadata_output_path, exist_ok=True)

# Define traits
traits = {
    "Chain": ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue", "original", "white"],
    "Earring": ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue", "original", "white"],
    "Crown": ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue", "original", "white"],
    "Sash": ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue", "original", "white"],
    "Band": ["green", "purple", "red", "yellow", "ash", "blue", "orange", "light_blue", "original", "white"]
}

nft_files = [f for f in os.listdir(output_images_path) if f.endswith(".png")]

# Select exactly 100 NFTs for rarity
selected_rarity_nfts = set(random.sample(range(len(nft_files)), 100))

for index, nft_file in enumerate(nft_files):
    nft_id = nft_file.split(".")[0]

    metadata = {
        "name": f"NFT #{nft_id}",
        "description": "This is a unique NFT from my collection.",
        "image": f"https://example.com/nft/{nft_file}",
        "attributes": []
    }

    for trait_type, values in traits.items():
        if index in selected_rarity_nfts:
            # Apply rarity to selected NFTs
            selected_value = random.choices(
                [random.choice(values[:8]), random.choice(values[8:])],
                weights=[0.95, 0.05]
            )[0]
        else:
            # Default to Group 1 for others
            selected_value = random.choice(values[:8])
        metadata["attributes"].append({
            "trait_type": trait_type,
            "value": selected_value
        })

    metadata_file_path = os.path.join(metadata_output_path, f"{nft_id}.json")
    with open(metadata_file_path, "w") as metadata_file:
        json.dump(metadata, metadata_file, indent=4)

print(f"Metadata for {len(nft_files)} NFTs saved in: {metadata_output_path}")