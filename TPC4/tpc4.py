import csv
import json
import re


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows


def write_json(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def parse_header(header_row):
    header = []
    for field in header_row:
        match = re.match(r"(.+)\{(\d+),(\d+)\}", field)
        if match:
            field_name = match.group(1)
            field_min = int(match.group(2))
            field_max = int(match.group(3))
            header.extend([f"{field_name}_{i}" for i in range(field_min, field_max+1)])
        else:
            header.append(field)
    return header


def parse_row(row, header):
    parsed_row = {}
    for i, value in enumerate(row):
        field_name = header[i]
        if "_" in field_name:
            match = re.match(r"(.+)_(\d+)", field_name)
            if match:
                field_name = match.group(1)
                field_index = int(match.group(2))
                if field_name not in parsed_row:
                    parsed_row[field_name] = []
                parsed_row[field_name].append(value)
                if field_index == len(parsed_row[field_name]):
                    parsed_row[field_name] = parse_field(parsed_row[field_name])
        else:
            parsed_row[field_name] = value
    return parsed_row


def parse_field(field):
    try:
        field = [float(x) for x in field]
        return {"sum": sum(field), "average": sum(field) / len(field)}
    except ValueError:
        return field


def csv_to_json(csv_path, json_path):
    rows = read_csv(csv_path)
    header = parse_header(rows[0])
    data = [parse_row(row, header) for row in rows[1:]]
    write_json(data, json_path)


if __name__ == "__main__":
    csv_to_json("alunos.csv", "alunos.json")
