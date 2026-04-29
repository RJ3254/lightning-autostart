#!/bin/bash
sudo apt update
sudo apt install python3-pip -y
python3 -m pip install lightning-sdk
export LIGHTNING_USER_ID="6f99046f-08a0-4c1f-9fc3-78b93ac2d99f"
export LIGHTNING_API_KEY="684bda97-11ec-4bea-ac9f-fbd7d61113b1"
lightning login
