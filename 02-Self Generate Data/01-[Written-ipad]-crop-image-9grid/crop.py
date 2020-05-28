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
    #print(filename)
    img = cv2.imread(filename)
    w, h = img.shape[0], img.shape[1]
    start1 = 0+boardersize
    end1 = w//3-boardersize
    start2 = w//3+boardersize
    end2 = w*2//3-boardersize
    start3 = w*2//3+boardersize
    end3 = w-boardersize
    
    grid1 = crop_img(start1, end1, start1, end1, img)
    grid2 = crop_img(start1, end1, start2, end2, img)
    grid3 = crop_img(start1, end1, start3, end3, img)
    
    grid4 = crop_img(start2, end2, start1, end1, img)
    grid5 = crop_img(start2, end2, start2, end2, img)
    grid6 = crop_img(start2, end2, start3, end3, img)
    
    grid7 = crop_img(start3, end3, start1, end1, img)
    grid8 = crop_img(start3, end3, start2, end2, img)
    grid9 = crop_img(start3, end3, start3, end3, img)
    
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
