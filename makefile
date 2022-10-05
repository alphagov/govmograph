out4.csv: headers.csv out3.csv
	cat headers.csv out3.csv > out4.csv

out.csv: data/embedded_links_structural_edgelist.tsv process_csvs.py
	./process_csvs.py data/embedded_links_structural_edgelist.tsv  

out2.csv: out.csv
	sort out.csv | uniq | tr -d '\r' > out2.csv

out3.csv: out2.csv
	cat out2.csv | grep -v "/guidance/using-open-document-formats-odf-in-your-organisation$$" | grep -v "/guidance/how-to-buy-printed-copies-of-official-documents$$"  | grep -v "/government/publications/environmental-permitting-public-participation-statement$$" > out3.csv
