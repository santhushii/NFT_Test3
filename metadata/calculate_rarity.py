# calculate_rarity.py
import os
import json
from collections import Counter

metadata_path = "E:/NFTTest3/metadata"
output_rarity_path = "E:/NFTTest3/metadata_with_rarity"

os.makedirs(output_rarity_path, exist_ok=True)

trait_counts = {}
total_nfts = 0

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

rarity_scores = {trait: {} for trait in trait_counts}
for trait_type, values in trait_counts.items():
    for trait_value, count in values.items():
        rarity_scores[trait_type][trait_value] = 1 / (count / total_nfts)

for metadata_file in os.listdir(metadata_path):
    if metadata_file.endswith(".json"):
        with open(os.path.join(metadata_path, metadata_file), "r") as f:
            metadata = json.load(f)

        total_rarity_score = 0
        for trait in metadata["attributes"]:
            trait_type = trait["trait_type"]
            trait_value = trait["value"]
            total_rarity_score += rarity_scores[trait_type][trait_value]

        metadata["rarity_score"] = total_rarity_score

        output_file_path = os.path.join(output_rarity_path, metadata_file)
        with open(output_file_path, "w") as f:
            json.dump(metadata, f, indent=4)

print(f"Rarity scores calculated and saved in: {output_rarity_path}")
