import os, json
import yaml

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
MANAGED_FEATURES_DIR = os.path.join(SCRIPT_DIR, 'managed-features')
FEATURES_DIR = os.path.join(SCRIPT_DIR, 'features')

def load_managed_features():
    managed_features = {}
    for filename in os.listdir(MANAGED_FEATURES_DIR):
        if filename.endswith('.yaml'):
            with open(os.path.join(MANAGED_FEATURES_DIR, filename), 'r') as f:
                managed_features.update(yaml.safe_load(f))
    return managed_features

def create_feature(feature_info):
    pass