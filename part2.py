import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("gene_table.txt", delimiter=",")

class Objective(ABC):
	@abstractmethod
	def record(self):
		pass

class Number(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		rows=str(self.f.shape[0])
		cols=str(self.f.shape[1])
		return pd.DataFrame(data=[[rows,cols],[]],columns=['Rows','Columns']).head(1)

class Semantics(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		semantics = list(self.f)
		sem_df = pd.DataFrame({'Labels': semantics})
		return sem_df

class Biotype(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		bio=self.f.groupby(['gene_biotype'])['gene_name'].count()
		bio=bio.sort_values().to_frame().reset_index()
		return bio.rename(columns={'gene_name':'Number of genes'})

class Associate(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		bio=self.f.groupby(['gene_biotype'])['gene_name'].count()
		bio=bio.sort_values().to_frame()
		bio['gene_biotypes'] = bio.index
		genes=[]
		for index, row in bio.iterrows():
			a=self.f.loc[:,['gene_biotype','gene_name']]
			a=a[a['gene_biotype']==row['gene_biotypes']] #filtering
			a=list(a.loc[:,'gene_name'])
			genes.append(a)
		bio['Gene_names']=genes
		bio=bio.loc[:,['Gene_names']]
		return bio

class Chromosome(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		return 'Number of chromosomes: '+ str(self.f.groupby(['chromosome']).count().shape[0])

class Genes_Chromosome(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		gene=self.f.groupby(['chromosome'])['gene_name'].count()
		gene=gene.sort_values().to_frame().reset_index()
		return gene.rename(columns={'gene_name':'Number of genes'})

class Plus(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		chrt=self.f.groupby(['chromosome'], as_index=False)['gene_name'].count()
		chrp=self.f.loc[:,['chromosome','strand']]
		chrp=chrp[chrp['strand']=='+']
		chrp2=chrp.groupby(['chromosome'], as_index=False)['strand'].count()
		conc=chrp2.merge(chrt,how='outer')
		conc['Plus_Percentage']=(conc['strand']/conc['gene_name']) * 100
		conc=conc.fillna(0)
		conc.sort_values(by='chromosome',inplace=True)
		return conc.rename(columns={'strand':'Plus strand', 'gene_name':'Number of genes','Plus_Percentage':'+ percentage'})

class Minus(Objective):
	def __init__ (self,f):
		self.f=f

	def record(self):
		chrt=self.f.groupby(['chromosome'], as_index=False)['gene_name'].count()
		chrm=self.f.loc[:,['chromosome','strand']]
		chrm=chrm[chrm['strand']=='-']
		chrm2=chrm.groupby(['chromosome'], as_index=False)['strand'].count()
		conc= chrm2.merge(chrt, how='outer')
		conc['Minus_Percentage']=(conc['strand']/conc['gene_name']) * 100
		conc= conc.fillna(0)
		conc.sort_values(by='chromosome', inplace=True)
		return conc.rename(columns={'strand':'Minus strand', 'gene_name':'Number of genes','Minus_Percentage':'- percentage'})