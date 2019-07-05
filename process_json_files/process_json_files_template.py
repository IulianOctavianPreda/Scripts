import json,sys,os 

# Recursive function to process all the values in a json
def processJson(data):
    for key in data:
        if isinstance(data[key],dict):
            # Action if the value is another json
            pass
        elif isinstance(data[key],list):
             # Action if the value is a list of jsons
            for i in range(0,len(data[key])):
                # Action for each json
                pass
        else:
            # Action if the value is just a value
            pass
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
    jsonFile.write(json.dumps(data,indent=2,sort_keys=True)) # Dumps the json with indentation and sorted by keys to be saved
    jsonFile.close()


if __name__ == '__main__':
    # Takes argumens: paths to files and folders 
    # Files will be processed imediately
    # Folders will be iterated and all the json files will be processed
    for arg in sys.argv:
        if arg.endswith('.json'):
            useJsonFile(arg)
        if arg.endswith('/'):
            for file in os.listdir(arg):
                if file.endswith('.json'):
                    useJsonFile(arg+file)
                