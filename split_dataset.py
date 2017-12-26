import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


from random import shuffle

# from xml_2_csv import main
# main()


def xml_full_list(data_path, path):
    # xml_list = []
    list_full_folders = []
    list_full_names = []
    for folder in path:
        folder_path = os.path.join(os.getcwd(), '{}'.format(data_path), '{}'.format(folder))
        print(folder_path)
        # print(glob.glob(folder_path+ '/*.xml'))
        # input()
        for xml_file in glob.glob(folder_path+ '/*.xml'):
            # print(xml_file)
            # print(os.path.basename(xml_file).split('.')[0] )
            # print(os.path.splitext(xml_file)[0])
            # print(os.path.dirname(xml_file))
            list_full_names.append(os.path.basename(xml_file).split('.')[0])
            list_full_folders.append(os.path.dirname(xml_file))
            # input()

    zip_lists = list(zip(list_full_names, list_full_folders))
    shuffle(zip_lists)

    list_full_names, list_full_folders = zip(*zip_lists)

    full_dataframe = pd.DataFrame({'path_folder': list_full_folders, 'files': list_full_names})
    full_dataframe.to_csv('full_files.csv', index=None)


    # print(len(list_full_folders))
    n_cut = int(((len(list_full_folders)*70)/100))
    # print(n_cut)
    n_cut2 = int((len(list_full_folders) - n_cut) / 2)

    train_dataframe = pd.DataFrame({'path_folder': list_full_folders[0:n_cut], 'files': list_full_names[0:n_cut]})
    train_dataframe.to_csv('train_files.csv', index=None)

    val_dataframe = pd.DataFrame({'path_folder': list_full_folders[n_cut:n_cut+n_cut2], 'files': list_full_names[n_cut:n_cut+n_cut2]})
    val_dataframe.to_csv('val_files.csv', index=None)

    test_dataframe = pd.DataFrame({'path_folder': list_full_folders[n_cut+n_cut2:len(list_full_folders)], 'files': list_full_names[n_cut+n_cut2:len(list_full_folders)]})
    test_dataframe.to_csv('test_files.csv', index=None)
        # list_full_folders.append(folder_path)
        
    # print(list_full_folders)
    # list_full_folders = shuffle(list_full_folders)
    # print(list_full_folders)
    # for xml_file in glob.glob(path + '/*.xml'):

data_path = 'FINAL Labelled Frames'
# data_path = os.path.join(os.getcwd(), '{}'.format(data_path))

list_folders = [dI for dI in os.listdir(data_path) if os.path.isdir(os.path.join(data_path,dI))]
print(list_folders)
shuffle(list_folders)
print(list_folders)

xml_full_list(data_path, list_folders)