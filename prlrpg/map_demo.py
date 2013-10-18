import yaml

from map import Map

if __name__ == '__main__':
    with open('sample_map.yaml') as f:
        data = yaml.load(f)
    map = Map(data)
    map.position.look()
    while True:
        direction = input()
        map.move(direction)
