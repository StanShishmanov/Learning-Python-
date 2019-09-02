data = input()
html_list = ["<!DOCTYPE html>", "<html>", "<head>", "</head>", "<body>", "</body>", "</html>"]
body_list = []
heading_counter = 1

while not data == "exit":
    tag = data.split(' ')[0]
    content = data.split(' ')[1]
    head = html_list[2]
    if tag == "title":
        content = f'    <title>{content}</title>'
        if tag not in html_list:
            html_list.insert(3, content)
        else:
            html_list[3] = content
    else:
        body_list.append(f"    <h{heading_counter}>{content}</h{heading_counter}>")
        heading_counter += 1
    data = input()
for i in body_list[::-1]:
    html_list.insert(5, i)
with open('index.html', 'w') as index_html:
    for i in html_list:
        index_html.writelines(i + '\n')











"""
"<!DOCTYPE html>
 <html>
 <head>
 </head>
 <body>
 </body>
 </html>
"""