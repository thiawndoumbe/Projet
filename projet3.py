import xml.etree.ElementTree as ET
import os
tree = ET.parse("tt\\train_zip\\train\\apple_1.xml")
root = tree.getroot()
from functools import reduce
print(root[0].text)
def findText(root,keys=[],vals=[]):
    """Cette fonction permet de retourner les tags et leurs valeurs dans une 
       pair (clé, valeur)
    """
    key = keys
    val = vals
    for child in root:
      #print('TAG :' + child.tag)
        key.append(child.tag)
        if child.text.strip():
            #print('TEXT : ' + child.text.strip())
            val.append(child.text.strip())
        else :
            val.append('nan')
        findText(child, key ,val)
    return (key, val)

def global_function(path_file):
    """Cette fonction a  pour but de creer un data frame pour un fichier xml donné
    param :
        path_file(str) : le chemin du fichier xml en str
    return:
        df(DataFrame) : data frame cree dont les columns sont les tags du fichier xml et les lignes representant les valeurs
            des tags.
    """
    tree = ET.parse(path_file)
    root = tree.getroot()
    # On appelle la fonction findText 
    (col, row) = findText(root, keys=[],vals=[])
    #print('(col, row)', (col, row))
    # creation du dataframe
    df = pd.DataFrame(row).T
    df.columns = col
    
    return df

def loop_file_location(path_directory_of_xml_file):
    """Cette fonction parcours le chemin absolue où est stocké les fichier xml et retourne 
    la dataframe global
    """
    #big list to stock all dataframe from xml file
    DATA = []
    fullname_list_path = []
    for filename in os.listdir(path_directory_of_xml_file):
      
        if not filename.endswith('.xml') : 
            continue
        else:
            print('filename, ', filename)
            fullname = os.path.join(path_directory_of_xml_file, filename)
            print('fullname, ', fullname) 
            fullname_list_path.append(fullname)
    print('fullname_list_path, ', fullname_list_path) 
    
    # On appel la fonction global_function pour créer une liste des dataframe
    DATA = [global_function(PATH) for PATH in fullname_list_path]
    
    # On combine toutes les dataframe creer pour former un seul dataframe
    df_final = reduce(lambda df1, df2: pd.concat([df1, df2], axis=0), DATA)
    return df_final
        

# Application    
path_directory_of_xml_file = 'tt\\train_zip\\train'
df = loop_file_location(path_directory_of_xml_file)
display(df)
