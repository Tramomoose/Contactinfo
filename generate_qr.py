import qrcode
import os

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
url = "https://tramomoose.github.io/Contactinfo/Contact.vcf"
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image in the same directory as the HTML file
output_path = os.path.join(os.path.dirname(__file__), "qr_code.png")
img.save(output_path)
