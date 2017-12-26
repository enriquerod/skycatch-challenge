import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        # print(xml_file)
        # print(os.path.basename(os.path.normpath(xml_file)))
        # print(os.path.basename(os.path.normpath(xml_file)).split('_')[1])
        leng = len(os.path.basename(os.path.normpath(xml_file)).split('_'))
        movie = os.path.basename(os.path.normpath(xml_file)).split('_')[leng - 1]

        movie = movie.split('.')[0]
        # print(movie)
        tree = ET.parse(xml_file)
        root = tree.getroot()
      
      
        for member in root.findall('object'):
            name = root.find('filename').text
            name = name + '_' + movie + '.jpg'
            value = (name,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for direct in ['train', 'valid', 'test']:
        image_path = os.path.join(os.getcwd(), '{}'.format(direct))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('{}.csv'.format(direct), index=None)
        print('Successfully converted xml to csv.')


main()