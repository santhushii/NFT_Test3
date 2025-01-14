import os
import json
from collections import Counter

# Paths
metadata_path = "E:/NFTTest3/metadata"
output_rarity_path = "E:/NFTTest3/metadata_with_rarity"

# Ensure output directory exists
os.makedirs(output_rarity_path, exist_ok=True)

# Step 1: Load Metadata and Count Trait Frequencies
trait_counts = {}
total_nfts = 0

# Count trait occurrences
for metadata_file in os.listdir(metadata_path):
    if metadata_file.endswith(".json"):
        total_nfts += 1
        with open(os.path.join(metadata_path, metadata_file), "r") as f:
            metadata = json.load(f)
            for trait in metadata["attributes"]:
                trait_type = trait["trait_type"]
                trait_value = trait["value"]
                if trait_type not in trait_counts:
                    trait_counts[trait_type] = Counter()
                trait_counts[trait_type][trait_value] += 1

# Step 2: Calculate Rarity Scores for Each Trait Value
rarity_scores = {trait: {} for trait in trait_counts}
for trait_type, values in trait_counts.items():
    for trait_value, count in values.items():
        rarity_scores[trait_type][trait_value] = 1 / (count / total_nfts)

# Step 3: Calculate Rarity Scores for Each NFT
for metadata_file in os.listdir(metadata_path):
    if metadata_file.endswith(".json"):
        with open(os.path.join(metadata_path, metadata_file), "r") as f:
            metadata = json.load(f)

        # Calculate total rarity score for the NFT
        total_rarity_score = 0
        for trait in metadata["attributes"]:
            trait_type = trait["trait_type"]
            trait_value = trait["value"]
            total_rarity_score += rarity_scores[trait_type][trait_value]

        # Add total rarity score to metadata
        metadata["rarity_score"] = total_rarity_score

        # Save updated metadata
        output_file_path = os.path.join(output_rarity_path, metadata_file)
        with open(output_file_path, "w") as f:
            json.dump(metadata, f, indent=4)

print(f"Rarity scores calculated and saved in: {output_rarity_path}")
