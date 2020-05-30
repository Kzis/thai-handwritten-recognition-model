import xml.etree.ElementTree as ET
import glob
import numpy as np
    
def xml_to_txt(xml_folder, folder_out):
    xml_paths = glob.glob(xml_folder+'/*.xml')
    for i in  range(len(xml_paths)):
        print(xml_paths[i])
        tree = ET.parse(xml_paths[i])
        root = tree.getroot()

        size = root.find('size')
        print(size.text)
        img_width = int(size.find('width').text)
        img_height = int(size.find('height').text)
        
        yolos = []
        for obj in root.findall('object'):
            name = obj.find('name').text
            if name == 'helmet':
                name = 1
            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)
            #x_center = (xmax + xmin)//2
            #y_center = (ymax + ymin)//2
            #x_center_rel = np.round(x_center/img_width, 6)
            #y_center_rel = np.round(y_center/img_height, 6)
            #width_rel = np.round((xmax - xmin)/img_width, 6)
            #height_rel = np.round((ymax - ymin)/img_height, 6)
            yolo = f"{name} {xmin} {xmax} {ymin} {ymax}"
            print(yolo)
            yolos.append(yolo)
        
        outpath = folder_out+"/"+xml_paths[i].split("\\")[1].split(".")[0]+".txt"
        print('out_path', outpath)
        with open(outpath, mode='wt') as f:
            f.write('\n'.join(yolos))
            
if __name__ == "__main__":
    xml_to_txt('ST200-1 xml', 'ST200-1 label')
