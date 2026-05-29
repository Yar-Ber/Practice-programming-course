import sys
import json

def setup_ai_model(): #Take the code in the def function
    config = {"model_name": "NeuralBrain-V0.1", "learning_rate": 0.1, "epochs": 100} #Dictionary for AI management
    
    print(f"Default configuration loaded: {config}")
    
    new_epochs = int(input("Enter new number of epochs: ")) 
    config["epochs"] = new_epochs #Change the value to a new one entered by the user
    
    batch_size = int(input("Enter batch size: ")) 
    config["batch_size"] = batch_size #Add a new key with the value
    
    return config

def config_json(config_data, file_path): #Take the code in the def function
    try: #Variables with validation
        with open (file_path, 'w') as file: #entering into a file
            json.dump(config_data, file, indent = 4)  #edit file
        print(f"Success: your config saved to {file_path}")

    except IOError as error: #Error checking
        print(f"Error: the config can't be saved. Details: {error}")
        sys.exit(1) #Emergency completion only on error

if __name__ == "__main__": #opening a file when it is directly opened
    config = setup_ai_model()
    config_json(config, 'config.json') #Function call