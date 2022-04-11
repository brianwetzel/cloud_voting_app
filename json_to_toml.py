import toml

# To run this script: Navigate to the correct folder in your terminal and enter "python json_to_toml.py" and hit enter

output_file = ".streamlit/secrets.toml"

with open("firestore-key.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)
