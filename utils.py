import os
import yaml

def load_family():
    family_files = os.listdir('config/family')
    
    family = []
    for file in family_files:
        with open(os.path.join('config/family', file), 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            family.append(data)
                
    return family