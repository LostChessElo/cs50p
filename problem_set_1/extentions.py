def extentions():
    extentions={
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf':'application/pdf',
        '.text':'text/plain',
        '.zip':'application/zip'
    }

    user_extention= input('File name: ').lower().strip().split('.')
    extention = '.' + user_extention[-1]
    if extention in extentions:
        return extentions[extention]
    else: 
        return 'application/octet-stream'


print(extentions())