from PIL import Image 
import os

data_dir = '../data'
#train_img_dir = os.path.join(data_dir, 'TrainIJCNN2013')
train_img_dir = "GTSDB"
png_img_dir = "GTSDB/png_data"


if os.path.exists(png_img_dir):
    shutil.rmtree(png_img_dir)
os.makedirs(png_img_dir) 

for img_name in os.listdir(train_img_dir):

#for img_name in ["00000.ppm","00001.ppm","00002.ppm"]:
    if img_name[-3:] == "ppm":
        img_path = os.path.join(train_img_dir, img_name)
        img = Image.open(img_path)
        png_path = os.path.join(png_img_dir, img_name[:-3]+'png')
        print(png_path)
        img.save(png_path)
        #img.show()
