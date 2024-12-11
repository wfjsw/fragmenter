import jsonlines
import shutil

with jsonlines.open('paths.jl', 'r') as reader:
    for obj in reader:
        print(obj['src'])
        shutil.copy(obj['path'], obj['src'])
