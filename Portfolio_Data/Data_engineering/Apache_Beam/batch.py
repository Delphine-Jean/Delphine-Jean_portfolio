#importation des packages apache beam
import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
from sys import argv

PROJECT_ID = 'projet-delphine'
# Définition du schema de notre dataset Bigquery de sortie 
SCHEMA = 'sr:INTEGER,abv:FLOAT,id:INTEGER,name:STRING,style:STRING,ounces:FLOAT'

#Définitions des fonctions de transformations que l'on souhaite utiliser dans notre pipleine
def suppr_null(data):
    "" "Filtre les enregistrements qui ne contiennent aucune information." ""
    return len(data['abv']) > 0 and len(data['id']) > 0 and len(data['name']) > 0 and len(data['style']) > 0


def convert(data):
    """Conversion des différents types de données."""
    data['abv'] = float(data['abv']) if 'abv' in data else None
    data['id'] = int(data['id']) if 'id' in data else None
    data['name'] = str(data['name']) if 'name' in data else None
    data['style'] = str(data['style']) if 'style' in data else None
    data['ounces'] = float(data['ounces']) if 'ounces' in data else None
    return data

def suppr_cols(data):
    'Suppression des collonnes inutiles'
    del data['ibu']
    del data['brewery_id']
    return data

# Construction de notre pipeline
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    known_args = parser.parse_known_args(argv)

    p = beam.Pipeline(options=PipelineOptions())

    (p | 'Lecture des données à partir du bucket Google cloud storage' >> beam.io.ReadFromText('gs://df-pipeline-1/batch/beers.csv', skip_header_lines =1)
       | 'Séparations des lignes' >> beam.Map(lambda x: x.split(','))
       | 'Transformation en dictionnaire (key-value)' >> beam.Map(lambda x: {"sr": x[0], "abv": x[1], "ibu": x[2], "id": x[3], "name": x[4], "style": x[5], "brewery_id": x[6], "ounces": x[7]}) 
       | 'Suppressions des lignes vides' >> beam.Filter(suppr_null)
       | 'Conversion des données' >> beam.Map(convert)
       | 'Suppression des collonnes inutiles' >> beam.Map(suppr_cols)
       | 'Ecriture des données dans Bigquery' >> beam.io.WriteToBigQuery(
           '{0}:beer.beer_data'.format(PROJECT_ID),
           schema=SCHEMA,
           write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

    # On charge notre pipeline dans notre runner via la méthon run
    result = p.run()
    result.wait_until_finish()
