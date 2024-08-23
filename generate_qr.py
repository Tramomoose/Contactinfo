import qrcode
import os
from datetime import datetime

# Data to encode in the QR code
data = "https://www.example.com"  # Replace with your desired link

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Save the QR code image in the /docs folder (which GitHub Pages uses)
output_dir = "docs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a unique filename based on the current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
file_path = os.path.join(output_dir, f"qr_code_{timestamp}.png")

# Save the image
img.save(file_path)

print(f"QR code saved to {file_path}")
