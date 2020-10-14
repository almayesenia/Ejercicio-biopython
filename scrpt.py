from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
def summarize_contents(filename):
all_s = []
r = list(SeqIO.parse(filename,"genbank"))
print("Path: ",os.path.dirname(filename))
print("Num_record = %i records" %len(r))
print("\n")
for seq_r in SeqIO.parse(filename,"genbank"):
	all_s.append(seq_r.name)
	print("Name: ",seq_r.name)
	print("ID :",seq_r.id)
	print("Location:")
	for seq_features in seq_r.features :
	print('Star: %d, Stop: %d' %(int(seq_feature.location.start),int(seq_feature.location.end)))
		
	
sunnarize_contents(filename)
