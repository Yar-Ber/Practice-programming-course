import sys

def setup_ai_model(): #Take the code in the def function
	config = {"model_name": "NeuralBrain-V0.1", "learning_rate": 0.1, "epochs": 100} #Dictionary for AI management

	print(f"Default configuration loaded: {config}")

	new_epochs = int(input("Enter new number of epochs: ")) 
	config["epochs"] = new_epochs #Change the value to a new one entered by the user

	batch_size = int(input("Enter batch size: ")) 
	config["batch_size"] = batch_size #Add a new key with the value

	return config

config = setup_ai_model() #Function call

print(f"Updated configuration: {config}")