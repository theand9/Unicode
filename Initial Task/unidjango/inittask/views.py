from datetime import datetime
import requests
from requests.exceptions import HTTPError
import json
from django.http import HttpResponse
from django.shortcuts import render


def getData(request):
    """This function retrieves SpaceX Launch Data from the SpaceX API using Python's Requests Module.

    Returns:
        final_Launch_Data[dict] -- Filtered Final Launch Data
    """

    filter_Query = "filter=mission_id,flight_number,launch_date_local,rocket/second_stage/payloads/manufacturer"
    url = f"https://api.spacexdata.com/v3/launches?{filter_Query}"
    final_Launch_Data = []

    json_Response = requests.get(url).json()
    # Only get entries when mission_id is not null and format date
    for i in json_Response:
        if i["mission_id"]:
            # Convert to Date Object
            i["launch_date_local"] = datetime.strptime(
                i["launch_date_local"][0:-3:] + i["launch_date_local"][-2::], "%Y-%m-%dT%H:%M:%S%z")
            # Format Date
            i["launch_date_local"] = i["launch_date_local"].strftime("%c")
            i["rocket"] = i["rocket"]["second_stage"]["payloads"]

            final_Launch_Data.append(i)

    return HttpResponse(final_Launch_Data)


def getDataTemplate(request):
    """This function retrieves SpaceX Launch Data from the SpaceX API using Python's Requests Module.

    Returns:
        final_Launch_Data[dict] -- Filtered Final Launch Data
    """

    filter_Query = "filter=mission_id,flight_number,launch_date_local,rocket/second_stage/payloads/manufacturer"
    url = f"https://api.spacexdata.com/v3/launches?{filter_Query}"
    final_Launch_Data = []

    json_Response = requests.get(url).json()
    # Only get entries when mission_id is not null and format date
    for i in json_Response:
        if i["mission_id"]:
            # Convert to Date Object
            i["launch_date_local"] = datetime.strptime(
                i["launch_date_local"][0:-3:] + i["launch_date_local"][-2::], "%Y-%m-%dT%H:%M:%S%z")
            # Format Date
            i["launch_date_local"] = i["launch_date_local"].strftime("%c")
            i["rocket"] = i["rocket"]["second_stage"]["payloads"]

            final_Launch_Data.append(i)

    return render(request, "task3.html", {"launch_Data": final_Launch_Data})
