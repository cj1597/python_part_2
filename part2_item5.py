import csv
import json


with open("input.json", 'r') as json_file:
    json_data = json.load(json_file)
    events = json_data["tracking_events"]

with open("output.csv", 'w', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    unique_keys = {x for y in events for x in y.keys()}
    csv_writer.writerow(unique_keys)

    # values = [row.get(key, '') for row in events for key in unique_keys]
    # csv_writer.writerow(values)
    # print(values)
    # values_list = []
    # for row in events:
    #     for key in unique_keys:
    #         values_list.append([row.get(key, '')])
    #     csv_writer.writerow(values_list)


    for row in events:
        for key in unique_keys:
            csv_writer.writerow([row.get(key, "")])


    # for y in events:
    #     for x in y.keys():
    #         print(x)


    #
    # for row in events:
    #     csv_writer.writerow(row.values())
    #
    # #ADD EMPTY STRING WHEN NO VALUE