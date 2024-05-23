import torch
from torchvision import models, transforms
from PIL import Image

def recognize_image(image_path):
    # Load a pre-trained image classification model from torchvision
    model = models.resnet50(pretrained=True)
    model.eval()

    # Define image transformations for preprocessing
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Load and preprocess the image
    image = Image.open(image_path)
    input_tensor = preprocess(image).unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)

    # Process the output to get the predicted class
    _, predicted_idx = torch.max(output, 1)
    predicted_class = predicted_idx.item()

    # You can use the ImageNet class labels to map the predicted class index to a human-readable label
    # For example, you can download the ImageNet labels file and use it to get the class label
    # For brevity, I'll skip this step in this example

    return predicted_class


