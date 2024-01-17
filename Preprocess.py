# FuzzTree
# Copyright (C) 2023 THEO BOURY 

import csv
import os
import shutil

import time
import pickle
import argparse
import networkx as nx
from FuzzTree import main
from VarnaDrawing import print_mapping_on_target_graph
from SliceInCubes import slicer


DEBUG=0
# A code on add artificial B53 ?
# A code to extract from the pdb ?
# A code to annotate the "pattern"?


def open_graph(graph_path):
    """
    Input: A graph path graph_path.
    Output: Returns graph G extracted from graphpath in a networkx format.
    """
    with open(graph_path,'rb') as f:
        G = pickle.load(f)
    return G

def slice_in_small_graphs(GPpath, GTpath, path="SmallGraphs", slice = 0, nb_procs = 1):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    GP = open_graph(GPpath)
    GT = open_graph(GTpath)
    graph_grid, Distancer = slicer(GP, GT, nb_procs, filename="", D = slice)
    for i, G in enumerate(graph_grid):
        with open(path + "/" + str(i), "wb") as f:
            pickle.dump(G, f)
    with open(path + "/" + "Distancer", "wb") as f:
        pickle.dump(Distancer, f)

parser = argparse.ArgumentParser()

parser.add_argument('--pattern', type=str, required=True)
parser.add_argument('--target', type=str, required=True)
parser.add_argument('--path', type=str, required=False)
parser.add_argument('--slice', type=str, required=False)
parser.add_argument('--procs', type=str, required=False)
args = parser.parse_args()

pattern = args.pattern
target = args.target 

path = "SmallGraphs"
slice = 1
nb_procs = 1

if args.path:
    path = args.path
if args.procs:
    nb_procs = int(args.procs)
if args.slice:
    slice = int(args.slice)

slice_in_small_graphs(pattern, target, path=path, slice = slice, nb_procs = nb_procs)

