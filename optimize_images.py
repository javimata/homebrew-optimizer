#!/usr/bin/env python3

import os
import argparse
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Optimize images in the current directory.")
    parser.add_argument('-o', '--output_dir', type=str, default='out', help="Output directory to save optimized images.")
    parser.add_argument('-f', '--format', type=str, help="Format to save images (e.g., 'JPEG', 'PNG').")
    parser.add_argument('-w', '--width', type=int, help="Width to resize images to.")
    parser.add_argument('-t', '--height', type=int, help="Height to resize images to.")
    parser.add_argument('-q', '--quality', type=int, default=85, help="Quality of the optimized images (1-100).")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help="Show program's version number and exit.")
    parser.add_argument('-r', '--report', type=bool, default=True, help="Show optimization report.")
    parser.add_argument('-n', '--nooverwrite', action='store_true', help="Don't overwrite existing files.")

    args = parser.parse_args()
    
    # Check if quality is within the valid range
    if args.quality < 1 or args.quality > 100:
        print("Error: The quality value most be between 1 and 100.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Process each image in the current directory
    for filename in os.listdir('.'):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join('.', filename)
            output_path = os.path.join(args.output_dir, filename)

            # Open the image
            img = Image.open(input_path)

            # Get the original dimensions of the image
            original_width, original_height = img.size

            # If only width is specified, calculate the height maintaining the original image aspect ratio
            if args.width and not args.height:
                height = int(original_height * args.width / original_width)
                img = img.resize((args.width, height))

            # If only height is specified, calculate the width maintaining the original image aspect ratio
            elif args.height and not args.width:
                width = int(original_width * args.height / original_height)
                img = img.resize((width, args.height))

            # If both width and height are specified, resize the image to these dimensions
            elif args.width and args.height:
                img = img.resize((args.width, args.height))

            # Change the output file extension if a format is specified
            if args.format:
                output_path = os.path.splitext(output_path)[0] + '.' + args.format

            # Save the image
            if args.format:
                format_lower = args.format.lower()
                if format_lower == 'jpeg' or format_lower == 'jpg':
                    img = img.convert('RGB')
                output_path = os.path.splitext(output_path)[0] + '.' + args.format

            # If nooverwrite is set and the output file exists, create a new file with a unique name
            if args.nooverwrite and os.path.exists(output_path):
                base, ext = os.path.splitext(output_path)
                i = 1
                while os.path.exists(output_path):
                    output_path = f"{base}_{i}{ext}"
                    i += 1

            if args.format:
                img.save(output_path, format_lower, quality=args.quality)
            else:
                img.save(output_path, quality=args.quality)

            # If report is enabled, print optimization details
            if args.report:
                original_size = os.path.getsize(input_path)
                final_size = os.path.getsize(output_path)
                optimization_percentage = 100 * (original_size - final_size) / original_size
                sign = '-' if final_size < original_size else ''
                print(f"\033[1;34m{filename}\033[0m | \033[1;32m{original_size} bytes\033[0m -> \033[1;34m{output_path}\033[0m | \033[1;32m{final_size} bytes\033[0m | \033[1;33m{sign}{optimization_percentage:.2f}%\033[0m")

if __name__ == "__main__":
    main()