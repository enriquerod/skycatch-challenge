import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


if not os.path.exists('train'):
    os.makedirs('train')


if not os.path.exists('valid'):
    os.makedirs('valid')

if not os.path.exists('test'):
    os.makedirs('test')


df_train = pd.read_csv('train_files.csv')
print(df_train.head())

for index, row in df_train.iterrows():
    path_jpg = os.path.join(row['path_folder'], '{}.jpg'.format(row['files']))
    path_xml = os.path.join(row['path_folder'], '{}.xml'.format(row['files']))
    movie = os.path.basename(os.path.normpath(row['path_folder']))
    file_name = row['files'] + '_' + movie
    # print(path_jpg)
    # print(path_xml)
    new_jpg = os.path.join('train', '{}.jpg'.format(file_name))
    new_xml = os.path.join('train', '{}.xml'.format(file_name))
    os.rename(path_jpg, new_jpg)
    os.rename(path_xml, new_xml)

   

df_train = pd.read_csv('val_files.csv')
print(df_train.head())

for index, row in df_train.iterrows():
    path_jpg = os.path.join(row['path_folder'], '{}.jpg'.format(row['files']))
    path_xml = os.path.join(row['path_folder'], '{}.xml'.format(row['files']))
    movie = os.path.basename(os.path.normpath(row['path_folder']))
    file_name = row['files'] + '_' + movie
    # print(path_jpg)
    # print(path_xml)
    new_jpg = os.path.join('valid', '{}.jpg'.format(file_name))
    new_xml = os.path.join('valid', '{}.xml'.format(file_name))
    os.rename(path_jpg, new_jpg)
    os.rename(path_xml, new_xml)
    

df_train = pd.read_csv('test_files.csv')
print(df_train.head())

for index, row in df_train.iterrows():
    path_jpg = os.path.join(row['path_folder'], '{}.jpg'.format(row['files']))
    path_xml = os.path.join(row['path_folder'], '{}.xml'.format(row['files']))
    movie = os.path.basename(os.path.normpath(row['path_folder']))
    file_name = row['files'] + '_' + movie
    # print(path_jpg)
    # print(path_xml)
    new_jpg = os.path.join('test', '{}.jpg'.format(file_name))
    new_xml = os.path.join('test', '{}.xml'.format(file_name))
    os.rename(path_jpg, new_jpg)
    os.rename(path_xml, new_xml)
    