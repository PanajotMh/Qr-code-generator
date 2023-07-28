import qrcode
import image

website = input("What website do you want me to turn into a qr code? : ")
box = int(input("What size? (Minimum 4/5 recommended): "))

qr = qrcode.QRCode(
    version = 22,
    box_size = box,
    border = 5
)

data = website

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", black_color="white")


img.show()
