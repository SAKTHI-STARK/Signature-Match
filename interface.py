import script2match as sp
import insert_db as ib
import retrieve as rt
import os
print("Signature Matching Model...")
print("press options")
def front_end():
    
    #get the option from the user to perform specific task
    n=int(input("1.Match signature \n2.Insert New Signature \n3.Exit \n******************\nEnter option:"))
    #condition based match and inserting new signature
    if n==1:
        id_no=int(input("Enter Id Number:"))
        database_signature_path=rt.retrieve_image(id_no,"temp_img.jpg")
        print("Enter the input directory")
        file_path=input()
        file_path=file_path.replace("\\","\\\\")
        file_path=file_path.replace('"',"")
        sp.main(file_path, "temp_img.jpg")
        os.remove("temp_img.jpg")
    elif n==2:
        dir_val=input("Enter the directory path of the image:")
        dir_val=dir_val.replace('"',"")
        ib.insert_image(dir_val)
    elif n==3:
        print("Exiting")
    else:
        print("Enter a valid input")
        front_end()
front_end()