def get_input(day):
    import os

    cache_file_name = 'day{0}.txt'.format(day)

    if not os.path.isfile(cache_file_name):
        import urllib.request
        import shutil

        url = "https://adventofcode.com/2018/day/{0}/input".format(day)
        req = urllib.request.Request(url)

        # cookie.txt should be in your .gitignore and contain 'session=<your advent of code session id>'
        with open('cookie.txt', 'r') as cookie:
            req.add_header('Cookie', cookie.read().strip())

        try:
            with urllib.request.urlopen(req) as input, open(cache_file_name, 'wb') as output:
                shutil.copyfileobj(input, output)
        except urllib.error.HTTPError as e:
            return

    with open(cache_file_name, 'rb') as input:
        return input.read().decode("utf-8").strip()
