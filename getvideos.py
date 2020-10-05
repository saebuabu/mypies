import urllib.request

# url2open = "https://embed-fastly.wistia.com/deliveries/6ddeeebf7fc041ea963a6ddd56ab15f1c20db7dc.m3u8/seg-{counter}-v1-a1.ts"
# url2open = "https://embedwistia-a.akamaihd.net/deliveries/ba8383cc5e493489bfb5609e406f9d3106d44c3b.m3u8/seg-{counter}-v1-a1.ts"
# filetowrite = "D:\\Downloads\\videos\\Day1_ReleasingAnxiety.ts"


allvideos = [
     {'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/741058b7d4b8f64bbda88feecdd81b64c1d5e44f.m3u8/seg-{counter}-v1-a1.ts',
      'maxcounter': 369,
      'toname': 'DailyPractice4'},
    {
        'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/b8ca7b3f9eac911678b940fc26dc8e2675d7678c.m3u8/seg-{counter}-v1-a1.ts',
        'maxcounter': 135,
        'toname': 'DailyMeditation4'},
    # {
    #    'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/5fddd3ba3d00b2bd908f51901c78f879963daa14.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 1465,
    #     'toname': 'BendingTwistingBalancingPress',
    #     },
    # {'fromurl': 'https://embed-fastly.wistia.com/deliveries/e20fb6304a59ea6117bfd88ad20dfe13f4ae926b.m3u8/seg-{counter}-v1-a1.ts',
    #   'maxcounter': 347,
    #   'toname': 'AnklePainAndStrengtening',
    #   },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/3b4c5a3b2525fa1b9c1818b74719bfeb0942876e.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 400,
    #     'toname': 'ShoulderPainAndStrengthening',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/ef995652b54675a6f6d725cba881f392b84094f8.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 300,
    #     'toname': 'WristPainAndStrengthening',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/849fa20ddc44c06eb8c19cb93e9aeb0d226f4b05.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 420,
    #     'toname': 'AidingDigestion',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/15b52f7a8c9aca3e1361db89dff8fe5bce6a3242.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 472,
    #     'toname': 'GettingQualitySleep',
    #  },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/09196812efa8c5a736be7db7dddcb35c2cce0a76.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 414,
    #     'toname': 'FindingYourInnerGround',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/8be858ab827b441732c6a21778d7fdbb21878039.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 411,
    #     'toname': 'OvercomingFear',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/fa60e27f89b86a55e5cfc35d89977d2f8e896fd2.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 392,
    #     'toname': 'EasingPain',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/e311a0cc8ea35ae3f65366181f43a3bc1578f87e.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 453,
    #     'toname': 'WorkingWithLoneliness',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/4a79a6a507ace30909e145b693d11d1745c3dccc.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 378,
    #     'toname': 'BeingWithTheUnknown',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/254c59662061cba0f206e26703bc6377c2c2d58a.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 386,
    #     'toname': 'CultivatingLongLastingHappiness',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/56db6da6b3759bad5e3b23f1f0548aabada9f10b.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 428,
    #     'toname': 'TheWarriorWithinLesson1',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/489c70990b24e5cb647fd57e9219a4a8b596659d.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 428,
    #     'toname': 'TheWarriorWithinLesson2',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/14ca27935e18d25a0eabf1f549dddcb31f42af07.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 435,
    #     'toname': 'JourneyToTheCoreLesson1',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/6fbfcc622cbde6364372a2a0a75cb9cea862efe6.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 435,
    #     'toname': 'JourneyToTheCoreLesson2',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/5d41003e0f200e64d794b20df7be503cc67f0efd.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 429,
    #     'toname': 'EnergizeTheArmsLesson1',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/930dc34bd191e7d0ba39e05d14a2259f7187e925.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 429,
    #     'toname': 'EnergizeTheArmsLesson2',
    # }
    # ,{
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/0e9e6a2e23a91e628e9b161d1d81254be6ad60c4.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 899,
    #     'toname': 'FindBeatBuildHeatLesson1',
    # }
    # ,
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/8b934c914d0f5e12d07e9f7f4c9244c9ed822424.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 897,
    #     'toname': 'BindAndRewind',
    # }
    # , {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/29d41b3664f6714ff1845f711d262e22d455e6ce.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 900,
    #     'toname': 'HipToTheFlow',
    # }
    # , {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/adf842e4d94fb6a21bdcd5c1b1e980a6c5e974ea.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 915,
    #     'toname': 'SuryaIntoTheSunset',
    # }
    # , {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/0678351f12fb5bfc35e35fb17badf2cfac0bc5d4.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 898,
    #     'toname': 'RockAndGlow',
    # }
    # , {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/fb152b07ae4ddebb8e3260366483f4f8416b35b6.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 897,
    #     'toname': 'StarLightFlight',
    # }
    # # tot hier dag 1 en dag 2 volledig
    # {
    #     'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/619b3dc7be9e1cc920d8f7784b3d82fa233b6bbc.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 411,
    #     'toname': 'Day3L1IgnotingYourPractice',
    # },
    # {
    #     'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/0993d1d1bc34c3b829d5cfcfecbc906612562968.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 456,
    #     'toname': 'Day3L2PoweredNPeaceful',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/fbc7ad4e51c3ec91666d030aee2fdf7f9ff644e4.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 964,
    #     'toname': 'Day3L3WorkingWheel',
    # },
    # {
    #     'fromurl': 'https://embed-fastly.wistia.com/deliveries/c35bf82d92b690e7e99b365bcc4b949af322dcf6.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 408,
    #     'toname': 'Day4L1WarmingIntoTheSideBody',
    # },
    # {
    #     'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/fb0de8d50f0d31c0e09fafe23382d08e77351b81.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 463,
    #     'toname': 'Day4L2SmoothSteadyHips',
    # },
    # {
    #     'fromurl': 'https://embedwistia-a.akamaihd.net/deliveries/dff41eb70539042835198f13ca32aa98e6595f79.m3u8/seg-{counter}-v1-a1.ts',
    #     'maxcounter': 1409,
    #     'toname': 'Day4L3HolyHandstands',
    # },
    # tot hier dag 3 en dag 4


]

for video in allvideos:
    url2open = video['fromurl']
    max = video['maxcounter']
    filetowrite = "D:\\Downloads\\videos\\" + video['toname'] + ".ts"
    counter = 1
    print(filetowrite + " started")
    while True:
        # counter <= max:
        # print(counter)
        url = url2open.replace("{counter}", str(counter))
        req = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(req)
        except:
            print("error with " + str(counter))
            counter += 1
            break

        the_page = response.read()
        # urllib.request.urlretrieve("https://embed-fastly.wistia.com/deliveries/6ddeeebf7fc041ea963a6ddd56ab15f1c20db7dc.m3u8/seg-"+ str(counter) + "-v1-a1.ts", "D:\\Downloads\\videos\\file" + str(counter) + ".ts")
        tsfile = open(filetowrite, 'ab')
        tsfile.write(the_page)
        counter += 1
    print(filetowrite + " is downloaded")

print("ready")
