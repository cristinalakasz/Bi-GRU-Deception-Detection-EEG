import os
import shutil
import pandas as pd

def eeg_csv_files(directory):
    """
    Returns a list of file paths for all EEG.csv files found in the given directory and its subdirectories.

    Args:
        directory (str): The directory to search for EEG.csv files.

    Returns:
        list: A list of file paths for all EEG.csv files found.

    """
    kept_files = []
    # Navigate through each folder and file in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # If the file is an EEG.csv file, add it to the list
            if file == 'EEG.csv':
                kept_files.append(os.path.join(root, file))
    return kept_files

# Call the function on the 'path' folder
# eeg_csv_files = eeg_csv_files('path')
# print(len(eeg_csv_files))


def remove_specific_files(directory):
    """
    Remove the files in the dataset that are not EEG.csv files.

    Args:
        directory (str): The directory path where the files are located.

    Returns:
        None
    """
    # List of files to remove
    files_to_remove = ['Gaze.csv', 'image.jpg', 'video.mp4']
    
    # Navigate through each folder and file in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # If the file is in the list of files to remove, delete it
            if file in files_to_remove:
                os.remove(os.path.join(root, file))

# Call the function on the absolute path to the dataset folder
# remove_specific_files('path')


def move_and_rename_files(directory):
    """
    Move and rename the 'EEG.csv' files in the specified directory.

    Args:
        directory (str): The directory path where the files are located.

    Returns:
        None
    """
    # Navigate through each folder and file in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # If the file is 'EEG.csv', move and rename it
            if file == 'EEG.csv':
                # Get the old file path
                old_file_path = os.path.join(root, file)
                # Get the new file name
                new_file_name = root.replace(directory, '').replace(os.sep, '_')[1:] + '_' + file
                # Get the new file path
                new_file_path = os.path.join(directory, new_file_name)
                # Move and rename the file
                shutil.move(old_file_path, new_file_path)

# Call the function on the absolute path to 'Finalized'
# move_and_rename_files('path')


def modify_annotation(csv_file):
    """
    Modifies the annotation CSV file by performing the following steps:
    1. Reads the CSV file.
    2. Removes the 'gaze', 'video', and 'image' columns.
    3. Removes rows where the 'EEG' column is null.
    4. Replaces the file paths in the 'EEG' column.
    5. Writes the updated data back to the CSV file.

    Args:
    - csv_file (str): The path to the annotation CSV file.

    Returns:
    None
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Remove 'gaze', 'video', and 'image' columns
    df = df.drop(columns=['gaze', 'video', 'image'])

    # Remove rows where the 'EEG' column is null
    df = df.dropna(subset=['eeg'])

    # Replace the file paths
    df = df.replace(to_replace=r'./Finalised/(User_\d+)/run_(\d+)/EEG.csv', 
                    value=r'./Finalised/\1_run_\2_EEG.csv', 
                    regex=True)

    # Write the updated data back to the CSV file
    df.to_csv(csv_file, index=False)

# Call the function on your CSV file
# modify_annotation('path')


# now I create the csv file Data, (initially it is a copy of Annotations.csv) where there will be the columns 
# "run", "usernum", all the channel columns fo each run and usernum pair 
# (contained in each designated file), and the lable "truth"

def create_data_file(Data_csv):
    # Read the Data.csv file
    data = pd.read_csv(Data_csv)

    # Initialize a list to store the data DataFrames
    data_frames = []

    # Loop through each row in the Data.csv DataFrame
    for index, row in data.iterrows():
        # Read the EEG data from the CSV file specified in the 'eeg' column
        eeg_data = pd.read_csv(row['eeg'])
        
        # Add the 'run', 'usernum', and 'truth' columns to the EEG data DataFrame
        eeg_data['run'] = row['run']
        eeg_data['usernum'] = row['usernum']
        eeg_data['truth'] = row['truth']
        
        # Append the EEG data DataFrame to the list
        data_frames.append(eeg_data)

    # Concatenate all the data DataFrames
    final_data = pd.concat(data_frames, ignore_index=True)

    # Overwrite the original Data.csv file with the final DataFrame
    final_data.to_csv(Data_csv, index=False)

    
create_data_file("C:/Users/crist/OneDrive/Desktop/TesiACSAI/code/src/Data.csv")