#!/usr/bin/env python3
import os
from PIL import Image

UPLOADED_IMAGE = "/Users/acebless/.gemini/antigravity/brain/e667cdff-c87f-4195-a5cb-75bbb81728d4/.user_uploaded/media__1785029075356.jpg"
OUTPUT_DIR = "/Users/acebless/Documents/Gemini/public/images/emails"

def main():
    if not os.path.exists(UPLOADED_IMAGE):
        print(f"Error: Uploaded image not found at {UPLOADED_IMAGE}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    img = Image.open(UPLOADED_IMAGE)
    w, h = img.size
    print(f"Image dimensions: width={w}, height={h}")

    # Top half contains the 8 templates.
    # The templates start slightly below the top header and end around the middle divider.
    # Let's inspect the layout:
    # Header title takes some vertical space (approx 8.5% of height)
    # The columns go down to the middle divider (approx 53.5% of height)
    
    top_y = int(h * 0.08)
    bottom_y = int(h * 0.54)
    column_width = w / 8
    
    names = [
        "email_lead_gen.jpg",
        "email_estimate_ready.jpg",
        "email_proposal_delivered.jpg",
        "email_project_update.jpg",
        "email_payment_reminder.jpg",
        "email_review_request.jpg",
        "email_newsletter.jpg",
        "email_project_complete.jpg"
    ]
    
    for i, name in enumerate(names):
        left_x = int(i * column_width)
        right_x = int((i + 1) * column_width)
        
        # Crop each column
        cropped = img.crop((left_x, top_y, right_x, bottom_y))
        output_path = os.path.join(OUTPUT_DIR, name)
        cropped.save(output_path, "JPEG")
        print(f"Saved: {output_path} ({cropped.size[0]}x{cropped.size[1]})")

    # Bottom left contains the map, bottom right contains stats/details.
    # Let's crop those too just in case!
    map_crop = img.crop((0, bottom_y, int(w * 0.55), h))
    map_crop.save(os.path.join(OUTPUT_DIR, "email_os_map.jpg"), "JPEG")
    print(f"Saved: email_os_map.jpg")
    
    laptop_crop = img.crop((int(w * 0.55), bottom_y, w, h))
    laptop_crop.save(os.path.join(OUTPUT_DIR, "email_os_laptop.jpg"), "JPEG")
    print(f"Saved: email_os_laptop.jpg")

if __name__ == "__main__":
    main()
