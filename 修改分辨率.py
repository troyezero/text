import glob
img_path = glob.glob("E:\WNCG\text1*.jpg")
path_save = "E:\WNCG\text1"
for file in img_path:
    name = os.path.join(path_save, file)
    im = Image.open(file)
    im.thumbnail((1920,1280))
    print(im.format, im.size, im.mode)
    im.save(name,'JPEG')