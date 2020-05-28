import cv2
import glob
import os

boardersize = 5
outputsize = 95


def crop_img(r_start, r_end, c_start, c_end, img):
    grid = img[r_start:r_end, c_start:c_end]
    grid = cv2.resize(grid, (outputsize, outputsize))
    return grid

def write_img(filename, folder_out):
    img = cv2.imread(filename)

    grid1 = crop_img(125, 420, 150, 500, img)
    grid2 = crop_img(125, 420, 520, 850, img)
    grid3 = crop_img(125, 420, 850, 1180, img)
    
    grid4 = crop_img(430, 700, 180, 500, img)
    grid5 = crop_img(430, 700, 520, 850, img)
    grid6 = crop_img(430, 700, 850, 1180, img)
    
    grid7 = crop_img(730, 970, 180, 500, img)
    grid8 = crop_img(730, 970, 520, 850, img)
    grid9 = crop_img(730, 970, 850, 1180, img)
    
    allgrid = [grid1, grid2, grid3,
               grid4, grid5, grid6,
               grid7, grid8, grid9]
    
    for num, grid in enumerate(allgrid):
        savename = folder_out+'/'+filename.split(".")[0]+str(num+1)+'.jpg'
        print(savename)
        cv2.imwrite(savename, grid)
        

filenames = glob.glob("*.jpg")
for filename in filenames:
    folder_name = filename.split("_")[0]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    write_img(filename, folder_name)
