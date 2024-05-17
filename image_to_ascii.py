from PIL import Image
    
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def downscale_image(image, scale):
    return image.resize((image.width // scale, image.height // scale))


def grayscale_image(image):
    return image.convert('L')


def pixel_to_ascii(pixel):
    return ASCII_CHARS[pixel // 23] 


def main(image, scale):
    dim = Image.open(image)
    im = downscale_image(dim, scale)
    imwidth = im.width
    gsim = grayscale_image(im)
    
    pixels = list(gsim.getdata())
    
    ascii_text = ''
    
    for pixel in pixels:
        ascii_text += pixel_to_ascii(pixel)
    
    ascii_img = '\n'.join([ascii_text[i:i+imwidth] for i in range(0, len(ascii_text), imwidth)])
        
    with open('ascii_lisa.txt', 'w') as writefile:
        writefile.write(ascii_img)
    
    print(im.size)
    
if __name__ == '__main__':
    main('mona_lisa.jpg', 2)
