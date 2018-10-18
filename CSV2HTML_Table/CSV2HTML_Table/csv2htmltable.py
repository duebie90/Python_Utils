import csv
import os

class csvReader:
    def __init__(self, csv_path):
        file = open(csv_path, "r")
        self.reader = csv.reader(file, delimiter=';', quotechar='|')

    def read(self):
        output_data = []
        for row in self.reader:
            output_data.append(row)
        return output_data

class CSV2HTML:
    def __init__(self, csv_path):
        self.csv_reader = csvReader(csv_path)
        self.input_data = self.csv_reader.read()
        output_dir = os.path.join("..", "output_html")
        try:
            os.makedirs(output_dir)
        except:
            pass
        output_filename = os.path.split(csv_path)[-1]
        output_filename = os.path.splitext(output_filename)[0]
        output_path = os.path.join(output_dir,output_filename+ ".html")
        self.html_file = open(output_path, 'w')

    def write_html(self):
        #self.html_file.write("<html>\n<head>\n</head>\n<body>")
        self.html_file.write("<table>\n")
        for line in self.input_data:
            line_string = "<tr>"
            for d in line:
                line_string += "<td>" + str(d) + "</td>"
            line_string += "</tr>\n"
            self.html_file.write(line_string)
        self.html_file.write("</table>\n")
        #self.html_file.write("</body>\n</html>")

    def __del__(self):
        self.html_file.close()


if __name__ == "__main__":
    # Hier den richtigen Dateinamen einfüllen

    input_dir = os.path.join("..","input_csv")
    try:
        os.makedirs(input_dir)
        print("Folder created. Please copy some cvs files into it.")
    except:
        pass
    files = os.listdir(input_dir)
    for f in files:
        file = os.path.join(input_dir, f)
        csv2html = CSV2HTML(file)
        csv2html.write_html()
