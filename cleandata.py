import json

# Path to the JSON file
file_path = '/Users/admin/PycharmProjects/HBAR/data.json'
output_file_path = '/Users/admin/PycharmProjects/HBAR/newdata.json'

# Function to load JSON data from file
def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Function to remove entries with positive transfers
def clean_positive_transfers(data):
    new_ids = []
    new_transfers = []
    new_timestamps = []
    
    for id, transfer, timestamp in zip(data['Transaction ID cryptotransfer'], data['Transfers'], data['Consensus Timestamp']):
        if not transfer.strip().startswith('+'):
            new_ids.append(id)
            new_transfers.append(transfer)
            new_timestamps.append(timestamp)
    
    data['Transaction ID cryptotransfer'] = new_ids
    data['Transfers'] = new_transfers
    data['Consensus Timestamp'] = new_timestamps

    return data

# Load the data
data = load_json_data(file_path)

# Clean the data
cleaned_data = clean_positive_transfers(data)

# Convert to JSON and save to a file
with open(output_file_path, 'w') as file:
    json.dump(cleaned_data, file, indent=4)

print(f'Data cleaned and saved to {output_file_path}')
