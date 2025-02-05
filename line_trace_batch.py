import cv2
import os
import datetime

def photo_to_line_art(image_path, output_path, low_threshold=50, high_threshold=150):
    """
    Convert a photo to line art using Canny edge detection.
    """
    # Load the image from disk
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply the Canny edge detector
    edges = cv2.Canny(blurred, low_threshold, high_threshold)
    
    # Invert the edge image (so we get dark lines on a light background)
    line_art = cv2.bitwise_not(edges)
    
    # Save the resulting line art image
    cv2.imwrite(output_path, line_art)
    print(f"Line art saved to {output_path}")

if __name__ == "__main__":
    # Define the input folder (e.g., '~/pepe') and output folder name
    input_folder = os.path.expanduser('~/pepe')
    output_folder = "line_trace"
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # List of acceptable image file extensions
    valid_extensions = ('.png', '.jpg', '.jpeg')
    
    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            # Full path to the input image
            input_path = os.path.join(input_folder, filename)
            
            # Generate a timestamp string (e.g., 20250205123045 for YYYYMMDDHHMMSS)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            
            # Split the filename into a base name and extension
            base_name, ext = os.path.splitext(filename)
            
            # Build the output file name: original name + _linetrace_ + timestamp + original extension
            output_filename = f"{base_name}_linetrace_{timestamp}{ext}"
            output_path = os.path.join(output_folder, output_filename)
            
            # Process the image and create the line art version
            photo_to_line_art(input_path, output_path)
