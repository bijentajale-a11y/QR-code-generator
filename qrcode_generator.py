import qrcode
import os
from qrcode.constants import ERROR_CORRECT_H

data=input("Enter the text or URL:").strip()#To get rid of any extra spaces
filename=input("Enter the file name:").strip()

# User can choose color
fill_color = input("QR color (default black): ").strip() or "black"
back_color = input("Background color (default white): ").strip() or "white"

if not filename.endswith(".png"):#Extension add automatically
    filename += ".png"

# Save in a folder automatically
folder = "generated_qr"
os.makedirs(folder, exist_ok=True)

filepath = os.path.join(folder, filename)

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color=fill_color, back_color=back_color)
image.save(filepath)


print(f"QR generated successfully as {filepath}.")

os.startfile(filepath)
