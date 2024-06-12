import os
from argparse import ArgumentParser

my_car_scenes = ["honda", "tesla"]

parser = ArgumentParser(description="Minimal evaluation script for my custom dataset")
parser.add_argument("--skip_training", action="store_true")
parser.add_argument("--skip_rendering", action="store_true")
parser.add_argument("--skip_metrics", action="store_true")
parser.add_argument("--output_path", default="./eval")
args, _ = parser.parse_known_args()

all_scenes = my_car_scenes

if not args.skip_training or not args.skip_rendering:
    args = parser.parse_args()

if not args.skip_training:
    common_args = " --quiet --eval --test_iterations -1 "
    for scene in my_car_scenes:
        source = "data/" + scene
        os.system("python train.py -s " + source + " -m " + args.output_path + "/" + scene + common_args)

if not args.skip_rendering:
    all_sources = ["data/" + scene for scene in my_car_scenes]

    common_args = " --quiet --eval --skip_train"
    for scene, source in zip(all_scenes, all_sources):
        os.system("python render.py --iteration 7000 -s " + source + " -m " + args.output_path + "/" + scene + common_args)

if not args.skip_metrics:
    scenes_string = " ".join([f"\"{args.output_path}/{scene}\"" for scene in all_scenes])

    os.system("python metrics.py -m " + scenes_string)
