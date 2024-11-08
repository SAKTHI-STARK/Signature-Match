import cv2
from skimage.metrics import structural_similarity as ssim
def preprocess_image(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    # Resize image to a fixed size
    img = cv2.resize(img, (300, 100))  
    # Apply Gaussian blur
    img = cv2.GaussianBlur(img, (5, 5), 0)   
    # Apply binary thresholding
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)   
    return img
def compare_signatures(img1, img2):
    # Use Structural Similarity Index (SSI) to compare images
    score, diff = ssim(img1, img2, full=True)
    return score
def main(input_signature_path, database_signature_path):
    # Preprocess both images
    input_signature = preprocess_image(input_signature_path)
    database_signature = preprocess_image(database_signature_path)
    # Compare the signatures
    similarity_score = compare_signatures(input_signature, database_signature)
    # Define a threshold for similarity
    threshold = 0.5  # Adjust this threshold based on your requirements
    # Print the result
    if similarity_score > threshold:
        print(f'Signature Match! Similarity Score: {similarity_score:.2f}')
    else:
        print(f'Signature Not Match. Similarity Score: {similarity_score:.2f}')
if __name__ == "__main__":
   pass
    