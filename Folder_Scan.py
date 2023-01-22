from PIL import Image
import imagehash
import os
import glob

#Please ensure to enter a full file path to the folder
scan_folder = input("Please enter the folder of images to be scanned: ")
filename = input("Please mention the file and filepath to save results in: ")
results = ""

#Changing the directory to the folder the user chose
os.chdir(scan_folder)

#The file the program is going to find a match for
image_file_to_match_hash = ""

#The for loop is going through all files in the folder with a .jpg extension
for image_file_to_match in glob.glob("*.jpg"):
    image_file_to_match_hash = imagehash.average_hash(
        Image.open(image_file_to_match))
    print("Finding a match for {0}".format(image_file_to_match))
    
    for image_scan in glob.glob("*.jpg"):
        if image_file_to_match != image_scan: 
            image_scan_hash = imagehash.average_hash(
                (Image.open(image_scan)))
            
            if image_file_to_match == image_scan_hash:
                results = results + \
                    "{0},{1},{2}\n".format(
                        image_scan, image_scan_hash, image_file_to_match)

print("The scan has been completed...")
print("*" * 50)
print("Saving results to {}".format(filename))  
f = open((filename), "w") #Writing the results to the results file
f.write("Matched fimage files found\n")
f.write("filename, hash, match file\n")
f.write(results)
f.close()