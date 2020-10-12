# Real-Time-Traffic-Sign-Detection
I have trained SSDlite-MobilenetV2 Model on GTSDB. I was able to achieve 75% mAP on testing dataset of GTSDB. It took me 22768 steps to train the model. Afterwards my validation accuracy started to decrease.  
The reason why i selected SSDlite because we made use of researchers work which shows that ssd-mobilnet is that fastest and lightest model in terms of memory consumption.Further details can be found in this link. https://github.com/aarcosg/traffic-sign-detection . In this link they have discussed about ssd model instead of ssdlite. SSDlite is slightly better in terms of FPS on embedded device. I also trained ssd-mobilenetv2 with ssdlite-mobilenetv2. Both have same mAP after training of model.While during implementation on raspberry pi 4 , we had 30% more FPS using ssdlite.  
Here are the steps i did in order to train a model:    
1. First of all i downloaded the GTSDB dataset from this link https://sid.erda.dk/public/archives/ff17dc924eba88d5d01a807357d6614c/published-archive.html  
2. The dataset is in PPM format so i converted it them to png format using the file (ppm to png.py).It is also given in above in my files section.  
3. Then i created tensorflow record(tfrecord) file.Generate_tfrecord.py is also provided above in order to convert images and csv file into tfrecord. You can take help from the link https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10  
4. After creating tfrecord file, i migrated to Google Colab since i didn't had access to heavy GPU and CPU.  
5. I used premium account in order to train the model.It took me 6-8 hours straight to train the model.  
6. I have also provided model config file in Model folder. You can download the model using this link of modelzoo  https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md  
7. I have attached the labelmap.pbtxt file which was used in order to train model on GTSDB.  
8. I trained the model twice.First time with training dataset(containing 600 images) and validation dataset(300 images which is originally for testing ).Once i got the approximate number of steps around which my model trained for the first time. On second run , i trained the model straight to that number of steps that is 22768.(The reason i didn't train the model in single run only because i had limited 900 pictures only in which 600 for training and 300 for testing. I didn't want to further split training dataset into (training and validation dataset).  
9. i have attached a picture in results folder of mAP calculated during first training run with name mAP1 ![alt text](https://https://github.com/bilal39/Real-Time-Traffic-Sign-Detection/blob/main/Results/mAP%20(validation%20dataset).jpeg?raw=true) and for second training i, mAP picture is named as mAP2.  
10. I have also attaced PR(precision recall) curves of it in the results folder.Testing samples are also attached in result folder.  
11. Inference graph of my model can be downloaded from this link. https://drive.google.com/file/d/1CEd_Grc3Vqmlmko0U6ggWEAtGspkwxrA/view?usp=sharing  
12. Then i implemented this model on raspberry pi 4. I got FPS from (1.6 - 2.1) FPS.  
13. I also added audio assist system to it. The model say out loud the name of the class of traffic sign it detected.  
