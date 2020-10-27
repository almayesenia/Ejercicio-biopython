def  resume_contents ( nombre de archivo ):
	listaOs  =  os . camino . split ( nombre de archivo )
	listaExt  =  os . camino . splitext ( nombre de archivo )
	si ( listaExt [ 1 ] ==  ".gbk" ):
		type_file =  "genbank"
	otra cosa :
		type_file =  "fasta"
	registro  =  lista ( SeqIO . parse ( nombre de archivo , tipo_archivo ))
	#Creacion de diccionario
	d  = {}
	d [ 'Archivo:' ] =  listaOs [ 1 ]
	d [ 'Ruta:' ] =  listaOs [ 0 ]
	d [ 'Num_records:' ] =  len ( registro )
	#Diccionario con listas
	d [ 'Nombres:' ] = []
	d [ 'ID:' ] = []
	d [ 'Descripciones' ] = []
	#Registro de records
	para  seq_rcd  en  SeqIO . analizar ( nombre de archivo , type_file ):
		d [ 'Nombres:' ]. append ( seq_rcd . Nombre )
		d [ 'ID:' ]. añadir ( seq_rcd . id )
		d [ 'Descripciones' ]. añadir ( descripción de seq_rcd . )
	volver  d
#Imprimir la funcion
si  name  ==  "main" :
	resultados  =  resume_contents ( nombre de archivo )
	imprimir ( resultados )
