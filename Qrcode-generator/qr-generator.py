import qrcode

def qrcode_generator(link):
    qr = qrcode.QRCode(version = 3, box_size = 5, border = 5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    name_qr = input('Enter the name for your file: ')
    img.save(name_qr + '.png')


if __name__ == "__main__":
    # loop
    exit = True
    while(exit):
        # input for the user to enter a link
        link =  input("Enter the link to transform to a QR-Code: ").strip()
        # This will check if its a valid link
        if link.endswith((".com",'.edu', '.io/page/#/')):
            # do this
            qrcode_generator(link)
            exit = False
        else:
            print("please enter a valid link")
            
