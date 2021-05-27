
# Installing SAP HANA 2.0 express edition on a precongigured VM - https://developers.sap.com/group.hxe-install-vm-xsa.html
# https://saphanajourney.com/hana-cloud/learning-article/using-jupyter-notebooks-with-sap-hana-cloud/#step-1

### Source: https://developers.sap.com/tutorials/hana-clients-python.html
### https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.02/en-US/f3b8fabf34324302b123297cdbe710f0.html

import hdbcli
import hana_ml

from hana_ml import dataframe
from hana_ml.dataframe import ConnectionContext
import pandas as pd

# connect to a SAP HANA DB
# conn2 = dataframe.ConnectionContext(address=’XXXX’, port=’XXXX’, user=’XXXX’, password=’XXXX’, encrypt='true', sslValidateCertificate='false')

flight_pd = pd.read_csv('travelroute.csv', sep=';', header=0, names=["CITYFROM","CITYTO", "NUMBOOKINGS"])

flight_hdf = dataframe.create_dataframe_from_pandas(conn2, flight_pd, 'TRAVEL_ROUTE2', 'XXXX', force=True, replace=True)
flight_hdf = conn2.table("TRAVEL_ROUTE2", schema="XXXX")
print(flight_hdf.select_statement)