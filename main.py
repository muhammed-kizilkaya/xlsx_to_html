import io
from xlsx_py import yazdir
# must be binary mode
xlsx_file = open('excel.xlsx', 'rb')
out_file = io.StringIO('out.html')

yazdir(xlsx_file, out_file, locale='tr')
print(out_file.getvalue())
out_file.seek(0)
with open('out.html', 'w') as f:
    f.write(out_file.getvalue())

result_html = out_file.read()

# console run code ->  python -m xlsx2html excel.xlsx output.html