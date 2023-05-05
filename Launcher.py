# FuzzTree
# Copyright (C) 2023 THEO BOURY 

import csv
import os
import time
import pickle
import argparse
from FuzzTree import main
from VarnaDrawing import print_mapping_on_target_graph


DEBUG=0

def open_graph(graph_path):
    """
    Input: A graph path graph_path.
    Output: Returns graph G extracted from graphpath in a networkx format.
    """
    with open(graph_path,'rb') as f:
        G = pickle.load(f)
    return G


def test_mapping(GPpath, GTpath, L, E, G, maxGAPdistance=3, nb_samples=1000, respect_injectivity=1, D = 5, Distancer_preprocessed = {}, nb_procs = 1):
    """
    Input: - A graph Pattern GP file named GPpath that we supposed to be exactly the pattern that we are looking for.
           - A RNA Target Graph GT file named GTpath. We are looking for GP or a fuzzy version of GP in it.
           - The Fuzzy Parameters L, E, G that are respectively threshold on sum of isostericity, number of edges and sum of gap distances.
           - maxGAPdistance and D, fuzzy parameter about how far we allow to look respectively for gaps and missing edges.
           - number of samples done for each searched pattern nb_samples.
           - A boolean respect_injectivity to ask if we want to ensure that the injectivity is respected or if we allow mapping with doublons.
           - strong_mapping indicates the proportion of the mapping that we want to be correct and the one that we allow to be "faulty".
           - If Distance in GT are already preprocessed, we cant ake them in input to avoid further computation in Distancer_preprocessed.
           - nb_procs, the number of processors allowed for precomputations.
    Output: Return the nb_samples mappings obtained for this instance.
    """
    GP = open_graph(GPpath)
    GT = open_graph(GTpath)
    timer = time.time()
    mapping = main(GP, GT, L, E, G, maxGAPdistance=maxGAPdistance, nb_samples=nb_samples, respect_injectivity=respect_injectivity, D = D, Distancer_preprocessed = Distancer_preprocessed, nb_procs = nb_procs)
    timer = time.time() - timer
    if DEBUG:
        print("\nmapping", mapping)
        print("\ntime", timer)
    return mapping

def test_varna(name_file,GPpath, GTpath, show=1, output_format='png', L = 0, E = 0, G = 0, maxGAPdistance=3, nb_samples=1000, respect_injectivity=1, D = 5, mapping = [], Distancer_preprocessed = {}, nb_procs = 1):
    """
    Input: - A filename for the graph name_file.
           - show to show the graph with matplotlib.pyplot.
           - output_format, specification of the type of storage for the graph.
           - mapping, the mapping that we ant to draw, if affected we discard the instance parameter, f not we compute a list of mappings for curent instance.
           - A graph Pattern GP file named GPpath that we supposed to be exactly the pattern that we are looking for.
           - A RNA Target Graph GT file named GTpath. We are looking for GP or a fuzzy version of GP in it.
           - The Fuzzy Parameters L, E, G that are respectively threshold on sum of isostericity, number of edges and sum of gap distances.
           - maxGAPdistance and D, fuzzy parameter about how far we allow to look respectively for gaps and missing edges.
           - number of samples done for each searched pattern nb_samples.
           - A boolean respect_injectivity to ask if we want to ensure that the injectivity is respected or if we allow mapping with doublons.
           - strong_mapping indicates the proportion of the mapping that we want to be correct and the one that we allow to be "faulty".
           - If Distance in GT are already preprocessed, we cant ake them in input to avoid further computation in Distancer_preprocessed.
           - nb_procs, the number of processors allowed for precomputations.
    Output: Return the Varna drawing for the mapping specified or for the first mapping in the list of mappings obtained for this instance.
    """
    GP = open_graph(GPpath)
    GT = open_graph(GTpath)
    if mapping:
        print_mapping_on_target_graph([], GT, mapping=mapping, output_format = output_format, name_file = name_file, show=show)
    else:
        print_mapping_on_target_graph(GP, GT, mapping = [], output_format = output_format, name_file = name_file, show=show, L=L, E=E, G=G, maxGAPdistance=maxGAPdistance, nb_samples=nb_samples, respect_injectivity=respect_injectivity, D = D, Distancer_preprocessed = Distancer_preprocessed, nb_procs = nb_procs)

parser = argparse.ArgumentParser()

parser.add_argument('--near', type=str, required=False)
parser.add_argument('--pattern', type=str, required=True)
parser.add_argument('--target', type=str, required=True)
parser.add_argument('--L', type=str, required=False)
parser.add_argument('--E', type=str, required=False)
parser.add_argument('--G', type=str, required=False)
parser.add_argument('--Dedge', type=str, required=False)
parser.add_argument('--Dgap', type=str, required=False)
parser.add_argument('--samples', type=str, required=False)
parser.add_argument('--usevarna', type=str, required=False)
parser.add_argument('--procs', type=str, required=False)
args = parser.parse_args()

pattern = args.pattern
target = args.target 

rm_near = True
if args.near == "True":
    rm_near = False

L = 20
E = 4
G = 20
Dedge = 5
Dgap = 10
nb_samples=1000
nb_procs = 1
if args.L:
    L = int(args.L)
if args.E:
    E = int(args.E)
if args.G:
    G = int(args.G)
if args.samples:
    nb_samples = int(args.samples)
if args.procs:
    nb_procs = int(args.procs)
if args.Dedge:
    Dedge = int(args.Dedge)
if args.Dgap:
    Dgap = int(args.Dgap)

if args.usevarna:
    test_varna("VarnaMapping", pattern, target, show=1, output_format="png",L=L, E=E, G=G, maxGAPdistance=Dgap, nb_samples=nb_samples, D = Dedge, nb_procs = nb_procs)
    if os.path.isfile("VarnaMapping.png"):
        print("You can see VarnaMapping.png for the mapping drawn with Varna.")
    else:
        print("No drawing as output, Varna is probably not set up yet.")
    
else:
    mappings = test_mapping(pattern, target, L=L, E=E, G=G, maxGAPdistance=Dgap, nb_samples=nb_samples, D = Dedge, nb_procs = nb_procs)
    print("Found mappings", mappings)
