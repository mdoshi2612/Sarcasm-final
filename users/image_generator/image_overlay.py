from PIL import Image, ImageDraw, ImageFont

def generate_image(pokemon, team_name):
    # Front Image
    filename1 = 'final1-01.png'
    
    # Back Image
    filename =  'pokemons/'+pokemon+'.png'
    
    # Open Front Image
    frontImage = Image.open(filename)
    
    # Open Background Image
    background = Image.open(filename1)

    # Convert image to RGBA
    frontImage = frontImage.convert("RGBA")
    #frontImage.show()


    # Convert image to RGBA
    background = background.convert("RGBA")
    #background.show()

    
    # Calculate width to be at the center
    width = (background.width - frontImage.width) // 2
    # Calculate height to be at the center
    height = (background.height - frontImage.height) // 2
    width_original,height_original=frontImage.size
    factor_1=1.3
    factor_2=1.3

    newsize = (int(factor_1*width_original),int(factor_2*width_original))
    frontImageScaled = frontImage.resize(newsize)

    # Paste the frontImage at (width, height)
    background.paste(frontImageScaled, (1900, 2300), frontImageScaled)
    #background.show()



    txt = Image.new("RGBA", background.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("AEH.ttf", 250)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    d.text((1700, 1900), "Team", font=fnt, fill=(255, 191, 0, 255))

    d.text((2400, 1900), team_name, font=fnt, fill=(255, 191, 0, 255))

    out = Image.alpha_composite(background, txt)
    return out
