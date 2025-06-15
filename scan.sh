echo -e "Starting scan..."

echo -e "Starting searching for secrets..."
strings ./model/pytorch_model.bin | grep -Ei 'token|key|AKIA|sk-|ghp_|Bearer|eyJ[a-zA-Z0-9._-]{10,}'
echo -e "Grep finished!"

echo -e "Running modelscan..."
python3 model_loader.py
.venv/bin/modelscan -p converted_model.pkl
echo -e "Scanning finished!"