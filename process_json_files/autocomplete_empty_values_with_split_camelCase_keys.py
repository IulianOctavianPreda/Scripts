import json,sys,re,os 

# Recursive function
# fills missing values with the key split into words by it's camel case format
def processJson(data):
    for key in data:
        if isinstance(data[key],dict):
            data[key] = processJson(data[key])
        elif isinstance(data[key],list):
            for i in range(0,len(data[key])):
                data[key][i] = processJson(data[key][i])
        else:
            if not len(data[key]):
                data[key] = re.sub("([a-z])([A-Z])","\g<1> \g<2>",key)
                data[key] = data[key].capitalize()
    return data                

# main json driver
def useJsonFile(arg):
    jsonFile = open(arg, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    data = processJson(data)

    ## Save our changes to JSON file
    jsonFile = open(arg, "w+")
    jsonFile.write(json.dumps(data,indent=2,sort_keys=True))
    jsonFile.close()


if __name__ == '__main__':
    for arg in sys.argv:
        if arg.endswith('.json'):
            useJsonFile(arg)
        if arg.endswith('/'):
            for file in os.listdir(arg):
                if file.endswith('.json'):
                    useJsonFile(arg+file)
                