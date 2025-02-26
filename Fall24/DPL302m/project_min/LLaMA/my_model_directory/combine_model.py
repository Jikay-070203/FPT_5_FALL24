import torch
from transformers import AutoModel

# Specify the correct directory containing your model files
model_directory = "D:/FPT/Kihoc/fall2024/DPL302m/LLaMA/my_model_directory/"  # Update with your actual folder name

# Load the models from the specified directory
models = [AutoModel.from_pretrained(model_directory) for _ in range(4)]  # Load the same model for demonstration

# Create an average model (or a custom merging strategy)
merged_model = models[0]

for model in models[1:]:
    for param1, param2 in zip(merged_model.parameters(), model.parameters()):
        param1.data += param2.data

# Save the merged model
merged_model.save_pretrained("merged_model")
