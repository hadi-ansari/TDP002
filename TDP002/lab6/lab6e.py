#! /usr/bin/env python3
import os, argparse



def copy_right_info(args):
    target_files = []
    file_extension = args.file_extension

    if os.path.isfile(args.destination) and file_extension in args.destination :
        target_files.append(args.destination)
        
    elif os.path.isdir(args.destination):
        list_item = os.listdir(args.destination)
        for item in list_item:
            splited_item = item.split(".")

            if len(splited_item) <= 2  and file_extension in splited_item[-1]:
                add_item = args.destination + "/" +item
                target_files.append(add_item)
        
    for i in target_files:
        name = i.split(".")
        new_file = name[0] + "." + args.new_extension
        with open(i, "r") as rf_target, open(args.copy_right_file,"r") as rf_info:
            with open(new_file, "w") as wf:
                look_for_end = False
                for line in rf_target:
                    if look_for_end == False:
                        wf.write(line)
                        if "BEGIN COPYRIGHT" in line:
                            for line in rf_info:
                                wf.write("# ")
                                wf.write(line)
                            rf_info.seek(0)
                            look_for_end = True
              
                    
                    elif "END COPYRIGHT" in line:
                        wf.write(line)
                        look_for_end = False
                    
                      
                

                    
                    
                


        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest = "copy_right_file")
    parser.add_argument(dest = "destination")
    parser.add_argument("-c", dest= "file_extension")
    parser.add_argument("-u", dest= "new_extension")
    args = parser.parse_args()
    copy_right_info(args)



#------------------------------ huvudprogram ------------------------------
if __name__ == "__main__":
        main()
