import json
import random
# Initialize an empty list to store the filtered elements
filtered_elements = []

# Read the JSONL file line by line
with open('human_evaluation_annotations.jsonl', 'r') as f:
    for line in f:
        try:
            # Parse each line as a JSON object
            element = json.loads(line)
            
            # Filter elements with the required condition
            statement_to_annotation = element['annotation']['statement_to_annotation']
            for statement_data in statement_to_annotation.values():
                citation_annotations = statement_data['citation_annotations']
                if citation_annotations:
                    put = False
                    for citation_annotation in citation_annotations:
                        citation_supports = citation_annotation['citation_supports']
                        if citation_supports == "Citation Completely Supports but Also Refutes Statement":
                            filtered_elements.append(element)
                            put = True
                            break
                    if put:
                        break
        except json.JSONDecodeError:
            # Handle any invalid JSON lines
            print("Invalid JSON object:", line)

# Randomly sample 30 elements from the filtered_elements list
sampled_elements = random.sample(filtered_elements, k=30)

# Save the sampled elements to a JSON file
with open('sampled_elements.json', 'w') as f:
    json.dump(sampled_elements, f)

# # Save the filtered elements to a JSON file
# with open('filtered_elements.json', 'w') as f:
#     json.dump(filtered_elements, f)
