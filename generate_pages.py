#!/usr/bin/env python3
"""
Run this script from the root of your repo to generate pages.json.
It scans the books_pages/ folder and lists all images in sorted order.

Usage:
    python generate_pages.py
    python generate_pages.py --title "My Book Title"
    python generate_pages.py --folder "books_pages" --title "War and Peace"
"""

import os
import json
import argparse

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'}

def generate(folder='books_pages', title='My Book'):
    if not os.path.isdir(folder):
        print(f"❌ Folder '{folder}' not found. Create it and add your images.")
        return

    images = sorted([
        f"{folder}/{f}"
        for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS
    ])

    if not images:
        print(f"⚠️  No images found in '{folder}'. Supported: jpg, png, webp, gif, avif")
        return

    data = {"title": title, "pages": images}

    with open('pages.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

    print(f"✅ pages.json generated with {len(images)} pages.")
    print(f"   Title: {title}")
    print(f"   First page: {images[0]}")
    print(f"   Last page:  {images[-1]}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate pages.json for the ebook reader.')
    parser.add_argument('--folder', default='books_pages', help='Image folder (default: books_pages)')
    parser.add_argument('--title', default='My Book', help='Book title (default: My Book)')
    args = parser.parse_args()
    generate(args.folder, args.title)
