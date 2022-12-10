#!/bin/bash
cd ../SpeakerRecognition
source ~/opt/anaconda3/etc/profile.d/conda.sh
conda activate soundslike
python SpeakerRecognition.py './data/user_data/input.wav' './data/admin_data/'