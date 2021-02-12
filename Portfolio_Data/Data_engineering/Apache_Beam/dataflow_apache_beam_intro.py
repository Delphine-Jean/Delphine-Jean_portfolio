# -*- coding: utf-8 -*-

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'projet-delphine'
google_cloud_options.job_name = 'pipeline-sanctions-police'
google_cloud_options.staging_location = 'gs://projet-delphine/df-pipeline-1'
google_cloud_options.temp_location = 'gs://projet-delphine/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'

p = beam.Pipeline(options=options)

pipeline_test =   (
                          p
                          | 'Lecture des données' >> beam.io.ReadFromText('gs://projet-delphine/df-pipeline-1/sanctionspolice.csv', skip_header_lines =1)
                          | 'Séparation des lignes' >> beam.Map(lambda x: x.split(','))
                          | 'Ecriture des données' >> beam.io.WriteToText('gs://projet-delphine/df-pipeline-1/sanctionspolice_output.csv')
                            

if __name__ == '__main__':
    run()

-