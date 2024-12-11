import glob
import os
import shutil
import jsonlines

bucket_index = 0
bucket_item = 0

with jsonlines.open('paths.jl', 'w') as writer:
    for path in glob.iglob("../**/*.php", recursive=True):
        with open(path, "r") as f:
            line1 = f.readline()
        if '//ICB0' not in line1:
            continue

        print(path)

        if bucket_item >= 100:
            bucket_index += 1
            bucket_item = 0

        unique_filename = f"{bucket_index}_{bucket_item}_{os.path.basename(path)}"
        os.makedirs(os.path.join('chunks', str(bucket_index)), exist_ok=True)
        destination_path = os.path.join('chunks', str(bucket_index), unique_filename)
        shutil.copy(path, destination_path)
        writer.write({'path': destination_path, 'src': path})
        bucket_item += 1
