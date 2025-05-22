import os
import pandas as pd

# Define dataset path
dataset_path = "op_spam_v1.4"

def load_reviews(folder_path, label):
    reviews = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                reviews.append((f.read(), label))
    return reviews

# Load all categories: positive/negative × truthful/deceptive
truthful_pos = load_reviews(os.path.join(dataset_path, "positive_polarity/truthful"), label=0)
deceptive_pos = load_reviews(os.path.join(dataset_path, "positive_polarity/deceptive"), label=1)
truthful_neg = load_reviews(os.path.join(dataset_path, "negative_polarity/truthful"), label=0)
deceptive_neg = load_reviews(os.path.join(dataset_path, "negative_polarity/deceptive"), label=1)

# Combine
data = truthful_pos + deceptive_pos + truthful_neg + deceptive_neg
df = pd.DataFrame(data, columns=["review", "label"])

# Save
df.to_csv("fake_reviews_dataset.csv", index=False)
print("✅ Dataset saved as fake_reviews_dataset.csv")
