

import qrcode
from PIL import Image

# The URL you want the QR code to point to
url = 'https://sustainsw.ac.uk'

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo or image you want to place in the middle of the QR code
logo_display = Image.open('QR/logo_sustainsw.png')

# Ensure the logo is in RGBA mode to handle any transparency
logo_display = logo_display.convert("RGBA")

# Calculate the maximum size of the logo
# max logo size is 1/3rd of the QR code size
logo_max_size = min(img.size) // 3

# If the logo is larger than the maximum size, resize it
logo_size = min(logo_max_size, logo_display.size[0], logo_display.size[1])
logo_display = logo_display.resize(
    (logo_size, logo_size), Image.Resampling.LANCZOS)

# Calculate position to place the logo at the center of the QR code
position = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

# Use the alpha channel of the logo as a mask for pasting
# The alpha channel is the 4th channel in "RGBA"
logo_mask = logo_display.split()[3]

# Paste the logo on the QR code using the alpha channel as the mask
img.paste(logo_display, position, logo_mask)

# Save the QR code with the logo to a file
img.save("QR/sustainsw_qr.png")
