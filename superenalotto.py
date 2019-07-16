from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


page_width = 99
page_height = 220
first_x = 11.75
first_y = 31.75
x_delta = 5.02
y_delta = 3.3
column_delta = 24.5


coords = {}


for num in range(1, 16):
    for row in range(0, 6):
        key = num + 15 * row
        coords[key] = (first_x+x_delta*(num-1), first_y+y_delta*row)


def get_coords(num, schedina_index):
    coord = coords[num]
    return (coord[0], coord[1] + schedina_index * column_delta)


def generate_report(columns, filename='schedina.pdf'):
    pagesize = (page_width * mm, page_height * mm)  # width, height
    doc = canvas.Canvas(
        filename,
        pagesize=pagesize)
    for schedina in [columns[i:i+5] for i in range(0, len(columns), 5)]:
        for schedina_index, column in enumerate(schedina):
            for number in column:
                x, y = get_coords(number, schedina_index)
                doc.circle(x*mm, (page_height-y)*mm, 0.5*mm, fill=1)
        doc.showPage()
    doc.save()


def print_file(filepath='colonne.txt', outputpath='schedine.pdf'):
    lines = []
    with open(filepath, 'r') as input_file:
        for line in input_file.readlines():
            splitted = line.split(' ')
            if splitted:
                lines.append(
                    sorted([int(item) for item in list(set(splitted))]))
    generate_report(lines, filename=outputpath)


if __name__ == '__main__':
    print_file()
