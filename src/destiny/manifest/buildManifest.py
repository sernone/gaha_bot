from ..classes import hashingData, d2Config
import requests, zipfile, os, pickle, json, sqlite3

def get_manifest():
    config = d2Config()
    headers = { 'X-API-Key': config.apiKey }
    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'

    #get the manifest location from the json
    r = requests.get(manifest_url, headers=headers)

    manifest = r.json()
    mani_url = 'http://www.bungie.net' + manifest['Response']['mobileWorldContentPaths']['en']

    #Download the file, write it to 'MANZIP'
    r = requests.get(mani_url)
    with open("./d2manifests/MANZIP", "wb") as zip:
        zip.write(r.content)
    print("Download Complete!")

    #Extract the file contents, and rename the extracted file
    # to 'Manifest.content'
    with zipfile.ZipFile('./d2manifests/MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    os.rename(name[0], './d2manifests/Manifest.content')
    print('Unzipped!')

def build_dict(hash_dict):
    #connect to the manifest
    con = sqlite3.connect('./d2manifests/manifest.content')
    print('Connected')
    #create a cursor object
    cur = con.cursor()

    all_data = {}
    #for every table name in the dictionary
    for table_name in hash_dict.keys():
        #get a list of all the jsons from the table
        cur.execute('SELECT json from '+table_name)
        print('Generating '+table_name+' dictionary....')

        #this returns a list of tuples: the first item in each tuple is our json
        items = cur.fetchall()

        #create a list of jsons
        item_jsons = [json.loads(item[0]) for item in items]

        #create a dictionary with the hashes as keys
        #and the jsons as values
        item_dict = {}
        hash = hash_dict[table_name]
        for item in item_jsons:
            item_dict[item[hash]] = item

        #add that dictionary to our all_data using the name of the table
        #as a key.
        all_data[table_name] = item_dict

    print('Dictionary Generated!')
    return all_data

def loadData():
    if os.path.exists('./d2manifests') == False:
        os.makedirs('./d2manifests')
        
    if os.path.isfile(r'./d2manifests/manifest.content') == False:
        get_manifest()
        hashing = hashingData.hashData()
        all_data = build_dict(hashing.hashes)
        with open('./d2manifests/manifest.pickle', 'wb') as data:
            pickle.dump(all_data, data)
            print("'manifest.pickle' created!\nDONE!")
    else:
        print('Pickle Exists')

    with open('./d2manifests/manifest.pickle', 'rb') as data:
        allData = pickle.load(data)

    return allData