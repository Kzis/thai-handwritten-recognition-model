import glob
import cv2

foldername = "ST200-1"
label_paths = glob.glob(foldername + " label/*.txt")


def crop_img(img, label_data):
    cls_name = label_data[0]
    if cls_name == 'ะ':
        cls_name = "อะ"
    if cls_name == 'า':
        cls_name = "อา"
    if cls_name == 'ำ':
        cls_name = "อำ"
    xmin = int(label_data[1])
    xmax = int(label_data[2])
    ymin = int(label_data[3])
    ymax = int(label_data[4])
    img_crop = img[ymin:ymax, xmin:xmax]
    img_crop = cv2.resize(img_crop, (95, 95))
    #cv2.imshow('crop', img_crop)
    return img_crop, cls_name
    

for label_path in label_paths:
    img_path = foldername+' img/'+ label_path.split('\\')[1].split('.')[0] + '.bmp'
    filename = label_path.split('\\')[1].split('.')[0]
    labels_data = []
    with open(label_path) as f:
        for row in f.readlines():
            labels_data.append(row.replace('\n', '').split(" "))
    img = cv2.imread(img_path)
    for idx, labels_data in enumerate(labels_data):
        img_crop, cls_name = crop_img(img, labels_data)
        out_folder = foldername+' img_out/'
        out_fname = cls_name+'_'+filename+'-'+str(idx)+'.jpg'
        savename = out_folder + out_fname
        print("crop img:", out_fname)
        cv2.imwrite(savename, img_crop)
