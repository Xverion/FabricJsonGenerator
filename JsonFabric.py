import json
import os

print("Do you want to generate a block or a item?")
print("1: Block")
print("2: Item")
Choice = int(input())

dir_path = os.path.dirname(os.path.realpath(__file__))

if Choice == 1 :
    print("Please enter the name of the block:")
    BLOCKNAME = str(input())

    print("Please enter the modid:")
    MODID = str(input())

    BLOCKLOC = f"{MODID}:block/{BLOCKNAME}"

    blockstate = {
        'variant':
            {'' :
                {'model': f'{BLOCKLOC}'}
            }
    }

    blockmodel = {
        'parent': 'block/cube_all',
        'textures':{
            'all': f'{BLOCKLOC}'
        }
    }

    itemmodel = {
        'parent': f"{BLOCKLOC}"
    }

    if not os.path.exists(f'{dir_path}/blockstates') :
        os.mkdir(f'{dir_path}/blockstates')

    with open(f'{dir_path}/blockstates/{BLOCKNAME}.json', 'w') as f:
        print(json.dump(blockstate, f, ensure_ascii=False, indent=4))
        f.close()

    if not os.path.exists(f'{dir_path}/models/block') :
        os.makedirs(f'{dir_path}/models/block')

    with open(f'{dir_path}/models/block/{BLOCKNAME}.json', 'w') as f:
        print(json.dump(blockmodel, f, ensure_ascii=False, indent=4))
        f.close()

    if not os.path.exists(f'{dir_path}/models/item') :
        os.makedirs(f'{dir_path}/models/item')

    with open(f'{dir_path}/models/item/{BLOCKNAME}.json', 'w') as f:
        print(json.dump(itemmodel, f, ensure_ascii=False, indent=4))
        f.close()


elif Choice == 2 :
    print("Please enter the name of the item:")
    ITEMNAME = str(input())

    print("Please enter the modid:")
    MODID = str(input())

    item = {
        'parent': 'item/generated',
        'textures': {
            'layer0': f'{MODID}:item/{ITEMNAME}'
        }
    }

    if not os.path.exists(f'{dir_path}/models/item') :
        os.makedirs(f'{dir_path}/models/item')

    with open(f'{dir_path}/models/item/{ITEMNAME}.json', 'w') as f:
        print(json.dump(item, f, ensure_ascii=False, indent=4))
        f.close()


else :
    print("please enter a valid number.")
