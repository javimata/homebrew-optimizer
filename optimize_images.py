#!/usr/bin/env python3

import os
import argparse
from PIL import Image

def optimize_image(input_path, output_path, width, height, quality, format):
    with Image.open(input_path) as img:
        # Resize image if width or height are specified
        if width or height:
            img = img.resize((width or img.width, height or img.height), Image.ANTIALIAS)
        
        # Save image with the specified quality and format
        img.save(output_path, format=format or img.format, quality=quality)

def main():
    parser = argparse.ArgumentParser(description="Optimize images in the current directory.")
    parser.add_argument('-o', '--output_dir', type=str, default='out', help="Output directory to save optimized images.")
    parser.add_argument('-f', '--format', type=str, help="Format to save images (e.g., 'JPEG', 'PNG', 'WEBP').")
    parser.add_argument('-w', '--width', type=int, help="Width to resize images to.")
    parser.add_argument('-t', '--height', type=int, help="Height to resize images to.")
    parser.add_argument('-q', '--quality', type=int, default=85, help="Quality of the optimized images (1-100).")

    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Process each image in the current directory
    for filename in os.listdir('.'):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            input_path = os.path.join('.', filename)
            output_path = os.path.join(args.output_dir, filename)
            
            # Determine the output format
            output_format = args.format if args.format else None
            
            try:
                optimize_image(input_path, output_path, args.width, args.height, args.quality, output_format)
                print(f"Optimized {filename} and saved to {output_path}")
            except Exception as e:
                print(f"Failed to optimize {filename}: {e}")

if __name__ == "__main__":
    main()

