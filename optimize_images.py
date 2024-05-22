#!/usr/bin/env python3

import os
import argparse
import imageio
from skimage.transform import resize

def main():
    parser = argparse.ArgumentParser(description="Optimize images in the current directory.")
    parser.add_argument('-o', '--output_dir', type=str, default='out', help="Output directory to save optimized images.")
    parser.add_argument('-f', '--format', type=str, help="Format to save images (e.g., 'JPEG', 'PNG', 'WEBP').")
    parser.add_argument('-w', '--width', type=int, help="Width to resize images to.")
    parser.add_argument('-t', '--height', type=int, help="Height to resize images to.")
    parser.add_argument('-q', '--quality', type=int, default=85, help="Quality of the optimized images (1-100).")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0', help="Show program's version number and exit.")

    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Process each image in the current directory
    for filename in os.listdir('.'):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            input_path = os.path.join('.', filename)
            
            # Change the output file extension if a format is specified
            if args.format:
                filename = os.path.splitext(filename)[0] + '.' + args.format.lower()

            output_path = os.path.join(args.output_dir, filename)

            # Read the image
            img = imageio.imread(input_path)

            # Resize the image if necessary
            if args.width or args.height:
                img = resize(img, (args.height or img.shape[0], args.width or img.shape[1]))

            # Save the image
            imageio.imsave(output_path, img, quality=args.quality)