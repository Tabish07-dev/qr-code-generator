import qrcode

data =input("Enter the data to encode in the QR code: ")
img=qrcode.make(data)
img.save("my-qr-code.png")
print("Qr code generated and saved as 'my-qr-code.png") 