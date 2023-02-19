from urllib3 import connection_from_url


i = 28
while i < 383:
    # url from commune
    filename = "https://embed-fastly.wistia.com/deliveries/6ddeeebf7fc041ea963a6ddd56ab15f1c20db7dc.m3u8/seg-" \
               + str(i) + "-v1-a1.ts"
    filetowrite = "D:\\Downloads\\videos\\yoga.ts"
    opener = con.build_opener()
    ts = opener.open(filename).read()
    # append stream to file
    tsfile = open(filetowrite, 'ab')
    tsfile.write(ts)
    print('part %s done!' % i)
    i += 1

print("ready downloading file")