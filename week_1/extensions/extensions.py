file_name = input('File name: ').lower().strip()
position = file_name.find('.')
file_type = file_name[position:]

match file_type:
    case '.gif':
        print('image/gif')
    case '.jpg' | '.jpeg':
        print('image/jpeg')
    case '.png':
        print('img/png')
    case '.pdf':
        print('application/pdf')
    case '.txt':
        print('text/plain')
    case '.zip':
        print('application/zip')
    case _:
        print('application/octet-stream')
