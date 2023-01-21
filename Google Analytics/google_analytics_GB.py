"""Hello Analytics Reporting API V4."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Build the service object.
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'gaapiaccessforpython-1d2e02237dfd.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    KEY_FILE_LOCATION, SCOPES)
service = build('analytics', 'v3', credentials=credentials)

# Establecer el ID de la vista de Google Analytics
view_id = '195738696'

# Establecer el período de tiempo para recuperar los datos
start_date = '30daysAgo'
end_date = 'today'

# Realizar una llamada a la API de Google Analytics para recuperar 
# los datos de la dimensión "Usuario"
results = service.data().ga().get(
    ids='ga:' + view_id,
    start_date=start_date,
    end_date=end_date,
    metrics='ga:users',
    dimensions='ga:userType'
).execute()


# Procesar los datos recuperados utilizando pandas
data = results.get('rows', [])
df = pd.DataFrame.from_records(data, columns=['userType', 'users'])

print(df.head(5))






'''
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    OrderBy,
)
import numpy as np
import pandas as pd
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gaapiaccessforpython-1d2e02237dfd.json"
property_id = "348915078"

client = BetaAnalyticsDataClient()

request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="sessionManualAdContent")],
    metrics=[Metric(name="sessions"), Metric(name="screenPageViewsPerSession")],
    date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
)


response = client.run_report(request)

print(response)



def sample_run_report(property_id="348915078"):
    """Runs a simple report on a Google Analytics 4 property."""
    # TODO(developer): Uncomment this variable and replace with your
    #  Google Analytics 4 property ID before running the sample.
    # property_id = "YOUR-GA4-PROPERTY-ID"

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    )
    response = client.run_report(request)

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)

sample_run_report()
'''
