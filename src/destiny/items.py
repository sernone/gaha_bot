from .manifest import loadData
import json


def getItem(itemName: str):
    itemName = itemName.lower()

    data = loadData()
    itemData = data['DestinyInventoryItemDefinition']
    itemFound = False

    for item in itemData:
        if 'name' in itemData[item]['displayProperties']:
            display = itemData[item]['displayProperties']
            if itemName == str(display['name']).lower():

                print('Name: ' + display['name'])
                print('Type: ' + itemData[item]['itemTypeAndTierDisplayName'])
                print(item)

                itemFound = True
                break

    if itemFound == False:
        print('Item not found ' + itemName)