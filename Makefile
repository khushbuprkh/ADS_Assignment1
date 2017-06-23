rawDataEda: dataIngestionTask
	python dataingestion.py

dataIngestionTask: 
	python dataingestion.py config.json
