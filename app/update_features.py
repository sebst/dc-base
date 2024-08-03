import os, json, shutil
import yaml

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
MANAGED_FEATURES_DIR = os.path.join(SCRIPT_DIR, '..', 'managed-features')
FEATURES_DIR = os.path.join(SCRIPT_DIR, '..', 'features')


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
    devcontainer_json = {}
    if 'brew' in feature_info.keys():
        package_name = feature_info['brew']['package']
        cmd = f"brew info --json {package_name}"
        result = os.popen(cmd).read()
        package_info = json.loads(result)[0]
        devcontainer_json['name'] = feature_info['name']
        devcontainer_json['id'] = feature_info['name']
        devcontainer_json['description'] = package_info['desc']
        devcontainer_json['documentationURL'] = package_info['homepage']
        devcontainer_json['version'] = "0.0.1"
        if "versioned_formulae" in package_info.keys():
            versions = [v.split("@")[1] for v in package_info["versioned_formulae"]]
            if versions:
                print(f"Versions: {versions}")
                devcontainer_json['options'] = {
                    "version": {
                        "type": "string",
                        "description": f"Version of {feature_info['name']} to install",
                        "default": versions[0],
                        "enum": versions
                    }
                }
    if devcontainer_json:
        os.makedirs(os.path.join(FEATURES_DIR,  feature_info['name']), exist_ok=True)
        with open(os.path.join(FEATURES_DIR,  feature_info['name'],  'devcontainer-feature.json'), 'w') as f:
            json.dump(devcontainer_json, f, indent=4)


def empty_feature_dir():
    # Recursively delete all directories in FEATURES_DIR:
    for root, dirs, files in os.walk(FEATURES_DIR, topdown=False):
        for name in dirs:
            shutil.rmtree(os.path.join(root, name))


def main():
    empty_feature_dir()
    managed_features = load_managed_features()
    for feature_info in managed_features.values():
        create_feature(feature_info)


if __name__ == '__main__':
    main()
