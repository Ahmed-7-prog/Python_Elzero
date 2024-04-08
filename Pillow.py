from PIL import Image , ImageFilter

#img_path=Image.open("download.png")
#img_path.show()
#img_path.save("PicTure.bmp")

before = Image.open("download.png")
# after = before.filter(ImageFilter.BoxBlur(4))
#after = before.convert("L")
#box=(0,0,500,500)
#after=before.crop(box)
# after=before.effect_spread(300)
after=before.resize([1000,1000])
after=before
after.show()