
import os
import shutil


def search_copy_LD (development_folder, destination_folder):
    
    # make sure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    print("Dev folder")
    # go through GXX folders
    print(os.listdir(development_folder))
    for gxx in os.listdir(development_folder):
        gxx_path = os.path.join(development_folder, gxx)
        print(gxx)
        # in group folder
        for folder in os.listdir(gxx_path):
            group_folder = os.path.join(gxx_path, folder)

            # if the folder inside of the GXX folder has "Experiments" in the title
            if "Experiments" in group_folder:
                print("EXPIR", group_folder)
                # go through all the experiment folders
                for expir in os.listdir(group_folder):
                        experiments = os.path.join(group_folder, expir)
                        print(experiments)
                        # if the experiment folder has "LD" in the title
                        if "LD" in experiments:

                            if "1. Protocol" in os.listdir(experiments):
                                protocol = os.path.join(experiments, "1. Protocol")
                                print("LD EXPIR:", protocol)

                            # go through files in protocol folder, only copy if excel
                                for file in os.listdir(protocol):
                                    if file.endswith((".xlsx", ".xlsm")):
                                       ld_file_path = os.path.join(protocol, file)

                                        # copy file to new folder
                                       shutil.copy(ld_file_path, os.path.join(destination_folder, file))
                                       print("Copied: {ld_file_path}")
                
                                

# Example usage:
development_folder = "U:\\Development Stuff Test"
destination_folder = "U:\\Extracted Protocols Test"

search_copy_LD(development_folder, destination_folder)
















