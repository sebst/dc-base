import os, json
import yaml

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
MANAGED_FEATURES_DIR = os.path.join(SCRIPT_DIR, 'managed-features')
FEATURES_DIR = os.path.join(SCRIPT_DIR, 'features')


def load_managed_features():
    managed_features = {}
    for filename in os.listdir(MANAGED_FEATURES_DIR):
        if filename.endswith('.yaml'):
            feature_name = filename.removesuffix('.yaml')
            with open(os.path.join(MANAGED_FEATURES_DIR, filename), 'r') as f:
                managed_features[feature_name] = yaml.safe_load(f)
                assert feature_name == managed_features[feature_name]['name']
    return managed_features


def create_feature(feature_info):
    with open(os.path.join(FEATURES_DIR, feature_info['name'] + '.json'), 'w') as f:
        f.write("\n")


def empty_feature_dir():
    for filename in os.listdir(FEATURES_DIR):
        if filename.endswith('.json'):
            os.remove(os.path.join(FEATURES_DIR, filename))


def main():
    empty_feature_dir()
    managed_features = load_managed_features()
    for feature_info in managed_features.values():
        create_feature(feature_info)


if __name__ == '__main__':
    main()
