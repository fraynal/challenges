import yaml

def parse_section(config_file, section):
    with open(config_file) as f:
        full_config = yaml.safe_load(f)
    return yaml.load(full_config[section], Loader=yaml.Loader)

conf = parse_section("config.yaml", "prod")
print("Config loaded:", conf)

