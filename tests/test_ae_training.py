import sys
import traceback
from autoencoder_training_main import main

if __name__ == '__main__':
    configurations = {
        # configurations for normal GAN
        'basic': ["path_dataset=../data/gansMultiCondition_SHORT.csv"],
        'load_checkpoint': ["path_dataset=../data/gansMultiCondition_SHORT.csv", "load_checkpoint"],
        'load_checkpoint_specific_file': ["path_dataset=../data/gansMultiCondition_SHORT.csv", "load_checkpoint", "path_checkpoint=trained_ae/checkpoint.pt"],
    }

    # general parameters
    n_epochs = 1
    batch_size = 32

    for key in configurations.keys():
        try:
            print(f"Running configuration {key}...")
            sys.argv = configurations[key] + [f"n_epochs={n_epochs}", f"batch_size={batch_size}"]
            main()
            print(f"\nConfiguration {key} finished successfully.\n\n")
        # if an error occurs, print key and full error message with traceback and exit
        except:
            print(f"Configuration {key} failed.")
            traceback.print_exc()
            exit(1)