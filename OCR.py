from tabula import read_pdf
from tabulate import tabulate
import pandas as pd

df = read_pdf("C:\\Users\\jayzo\\Downloads\\llm_sample_dataset.pdf", pages='1')
df = df[0]

x = list(df.columns)

new_row = pd.DataFrame({'applicant_id': x[0], 'application_date': x[1], 'age': x[2],
                        'cibil_score': x[3], 'loan_type': x[4], 'loan_amount': x[5]},
                       index=[0])

df = df.set_axis(['applicant_id', 'application_date', 'age', 'cibil_score', 'loan_type', 'loan_amount',
                  'interest_rate'], axis=1)

df = pd.concat([new_row, df]).reset_index(drop=True)

# for i in range(2, 5):
#     xdf = read_pdf("C:\\Users\\jayzo\\Downloads\\llm_sample_dataset.pdf", pages=i)
#     xdf = xdf[0]
#
#     x = list(df.columns)
#     xnew_row = pd.DataFrame({'applicant_id': x[0], 'application_date': x[1], 'age': x[2],
#                              'cibil_score': x[3], 'loan_type': x[4], 'loan_amount': x[5]},
#                             index=[0])
#
#     xdf = df.set_axis(['applicant_id', 'application_date', 'age', 'cibil_score', 'loan_type', 'loan_amount',
#                        'interest_rate'], axis=1)
#
#     xdf = pd.concat([xnew_row, xdf]).reset_index(drop=True)
#     print(xdf)
#     # df = pd.concat([df, xdf]).reset_index(drop=True)

print(df)













#
# def async_detect_document(gcs_source_uri, gcs_destination_uri):
#     """OCR with PDF/TIFF as source files on GCS"""
#     import json
#     import re
#     from google.cloud import vision
#     from google.cloud import storage
#
#     # Supported mime_types are: 'application/pdf' and 'image/tiff'
#     mime_type = "application/pdf"
#
#     # How many pages should be grouped into each json output file.
#     batch_size = 2
#
#     client = vision.ImageAnnotatorClient()
#
#     feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
#
#     gcs_source = vision.GcsSource(uri=gcs_source_uri)
#     input_config = vision.InputConfig(gcs_source=gcs_source, mime_type=mime_type)
#
#     gcs_destination = vision.GcsDestination(uri=gcs_destination_uri)
#     output_config = vision.OutputConfig(
#         gcs_destination=gcs_destination, batch_size=batch_size
#     )
#
#     async_request = vision.AsyncAnnotateFileRequest(
#         features=[feature], input_config=input_config, output_config=output_config
#     )
#
#     operation = client.async_batch_annotate_files(requests=[async_request])
#
#     print("Waiting for the operation to finish.")
#     operation.result(timeout=420)
#
#     # Once the request has completed and the output has been
#     # written to GCS, we can list all the output files.
#     storage_client = storage.Client()
#
#     match = re.match(r"gs://([^/]+)/(.+)", gcs_destination_uri)
#     bucket_name = match.group(1)
#     prefix = match.group(2)
#
#     bucket = storage_client.get_bucket(bucket_name)
#
#     # List objects with the given prefix, filtering out folders.
#     blob_list = [
#         blob
#         for blob in list(bucket.list_blobs(prefix=prefix))
#         if not blob.name.endswith("/")
#     ]
#     print("Output files:")
#     for blob in blob_list:
#         print(blob.name)
#
#     # Process the first output file from GCS.
#     # Since we specified batch_size=2, the first response contains
#     # the first two pages of the input file.
#     output = blob_list[0]
#
#     json_string = output.download_as_bytes().decode("utf-8")
#     response = json.loads(json_string)
#
#     # The actual response for the first page of the input file.
#     first_page_response = response["responses"][0]
#     annotation = first_page_response["fullTextAnnotation"]
#
#     # Here we print the full text from the first page.
#     # The response contains more information:
#     # annotation/pages/blocks/paragraphs/words/symbols
#     # including confidence scores and bounding boxes
#     print("Full text:\n")
#     print(annotation["text"])
#
#
# async_detect_document("C:\\Users\\jayzo\\Downloads\\llm_sample_dataset.pdf",
#                       "C:\\Users\\jayzo\\Downloads\\llm_sample_dataset.json")