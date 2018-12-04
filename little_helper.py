def get_input(day, year=2018):
    import os

    cache_file_name = 'day{0}.txt'.format(day)

    if not os.path.isfile(cache_file_name):
        import urllib.request
        import shutil

        url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
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


def submit(answer, level, day, year=2018, reopen=True):
    """
    Based on wimglenn's aocd.py
    """
    import requests
    import bs4
    import webbrowser

    if level not in {1, 2}:
        raise ValueError("level must be 1 or 2")
    url = "https://adventofcode.com/{0}/day/{1}/answer".format(year, day)

    with open('cookie.txt', 'r') as cookie:
        session_string = cookie.read().strip()
        if session_string.startswith("session="):
            session = session_string[8:]
    response = requests.post(
        url,
        cookies={"session": session},
        headers={"User-Agent": "little_helper.py/v1"},
        data={"level": level, "answer": answer},
    )
    if not response.ok:
        raise RuntimeError("Non-200 response for POST: {}".format(response))
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    message = soup.article.text
    if "That's the right answer" in message:
        if reopen:
            webbrowser.open(response.url)  # So you can read part B on the website...
    return message
