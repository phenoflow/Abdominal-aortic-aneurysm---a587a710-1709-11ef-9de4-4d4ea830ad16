# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7A13.11","system":"readv2"},{"code":"96654","system":"readv2"},{"code":"63408","system":"readv2"},{"code":"66232","system":"readv2"},{"code":"45474","system":"readv2"},{"code":"17220","system":"readv2"},{"code":"69922","system":"readv2"},{"code":"92925","system":"readv2"},{"code":"54192","system":"readv2"},{"code":"31613","system":"readv2"},{"code":"45477","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-aortic-aneurysm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-aortic-aneurysm-repair---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-aortic-aneurysm-repair---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-aortic-aneurysm-repair---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
