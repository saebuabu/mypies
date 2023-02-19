import sys

import urllib3

i = 1
while i < 9:
    # url from commune

    filename = "https://connect-prd-cdn.unity.com/20210429/videos/921c0c64-b8e9-443a-b816-7a5ad9b78b5f_1.4_step_into_driver_seat_v3/vod15/origin/fs" + str(i) + ".ts?connect_token=exp=1647783719~acl=/20210429/videos/921c0c64-b8e9-443a-b816-7a5ad9b78b5f_1.4_step_into_driver_seat_v3/vod15/origin/fs"\
              + str(i) + ".ts~hmac=111efd7c1f1337c375c3255bc048e51ec524eb647444a5e69fcfd062c771c05d"

    filetowrite = "D:\\Downloads\\videos\\unity1.ts"

    #opener = connection_from_url.build_opener()
    ts = urllib3.opener.open(filename).read()
    # append stream to file
    tsfile = open(filetowrite, 'ab')
    tsfile.write(ts)
    print('part %s done!' % i)
    i += 1

print("ready downloading file")