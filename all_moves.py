import yaml

with open('./all_moves.yml', 'r') as stream:
  moves = yaml.safe_load(stream)
