import requests


def download_raw_data(url):
    cookies = {
        's_fid': '582F41E5B5EE3F91-06D2B37F363E3DB1',
        '_ga': 'GA1.2.1330760792.1584017985',
        '_socrata_session_id': 'BAh7CEkiD3Nlc3Npb25faWQGOgZFRkkiJTJmODQ1NzVkOTliMTkwYThlMGMyMjIzZDZlNzI3MjIyBjsARkkiCXVzZXIGOwBGMEkiEF9jc3JmX3Rva2VuBjsARkkiMUNUc2JQQmc2ZGRyVW1YN29lYU4zMnJWZHNHbk9zeHZyaitWZER3T1crOXM9BjsARg%3D%3D--0482c883277b0b57ac3ac777eedfbf4ca9195a0f',
        '_gid': 'GA1.2.681595992.1587979645',
        's_vnum': '1588280400166%26vn%3D4',
        's_invisit': 'true',
        's_lv_s': 'Less%20than%207%20days',
        's_visit': '1',
        's_cc': 'true',
        '_4c_': 'hVPfb6JAEP5XGh76VGBZFtg1aS4qWG1aacXL5fpCBNayJwUCCPUa%2F%2FebFayXNLnzxW%2BGmW9%2B7HwfSpfyXBkZFnWYwxiymeHcKDt%2BqJXRh1KJRP61ykjhzMEsjk0V062tkoRTlTJKVNMxkbXBiRmzSLlR3iUXcDCTMWwh43ijxOXA8aHsqwyo0qYp65Gud12nxUmsvRatnsdpredtXettXVV6XLQiCTvOd9lBB9qx60%2B8MPCCYOEvw4ULLBbFM2J41sTyPHPGDBXZLp6Yzsy0Tc90JwakxUXCIdRgmqPZYDe%2FpUURwLIqkn3chM2hlCEdj67qZAcfEt6KmIedSJoUPmDLRhdvysVr2kgSQk7uspKGhi0wOpEnRXfJRIRevJdMhAi410W5Flxmg%2BEH3kMwwLE77dEs2wP4CWg5nc%2BD9VPvXuS%2F9tWhx97TqgfT4u1tn4vmcLcXp5GlL62KXMS9sZwuVu4nnfdyWuGp8vphPZS%2By4pok835Jjv1L9e%2BDtzVmcCb9ygoN7moh4jHxx%2BrgXYiqiZ1%2BZbHTT3kLPxgSPKf5ude%2FanvD8mLYED3RTTkvIjdpkdRVXT1aUNykjd%2BdXq3QsY9iHz%2FDkYF1arqvMVaNHL04aQGB5xy75OVH9ercOKNp%2F7yrzOU8YaBNVw4Ws4bPdLhCsEpz9LQ7wMVa0hDem1RYiHiWBQhZBvfxs%2BTW%2BN6K5Lb%2F17i9fjZu5X3WEolYQBZEW8y2SyIDxY%2FDr%2BfHsQwTeTYyGFYA0USBDqilnIcZEUpsm1ECbYsOOUGpERtguQPIlpxViqOHexgSlXGE6QSa2OroGui2lvHxIkdRVuTnJUKqqcGAUqTDJQGPTOW2cBoXIIZQTaM65yDyWf9sh2i8Zduza%2Fd9m8bwpb%2FkfdlyuPxDw%3D%3D',
        's_ppvl': 'Provisional%2520Death%2520Counts%2520for%2520Coronavirus%2520Disease%2520%2528COVID-19%2529%2520%257C%2520Data%2520%257C%2520Centers%2520for%2520Disease%2520Control%2520and%2520Prevention%2C22%2C97%2C8593%2C2560%2C1255%2C2560%2C1440%2C1%2CL',
        'socrata-csrf-token': '1gjO3YM5iXq6bXcVstveWzflQBesb9D/YC890uLBXE/fM9XhmwP8oG70Cf3LeKmBgrjwfmLcyxTvymDd4VenlA==',
        's_ptc': '0.00%5E%5E0.01%5E%5E0.18%5E%5E0.54%5E%5E1.48%5E%5E0.97%5E%5E3.84%5E%5E0.01%5E%5E6.08',
        'gpv_c54': 'https%3A%2F%2Fdata.cdc.gov%2FNCHS%2FProvisional-Death-Counts-for-Coronavirus-Disease-C%2Fhc4f-j6nb',
        'gpv_v45': 'Provisional%20Death%20Counts%20for%20Coronavirus%20Disease%20%28COVID-19%29%20%7C%20Data%20%7C%20Centers%20for%20Disease%20Control%20and%20Prevention',
        's_lv': '1587979988970',
        's_sq': '%5B%5BB%5D%5D',
        's_tps': '78',
        's_pvs': '273',
        's_ppv': 'Provisional%2520Death%2520Counts%2520for%2520Coronavirus%2520Disease%2520%2528COVID-19%2529%2520%257C%2520Data%2520%257C%2520Centers%2520for%2520Disease%2520Control%2520and%2520Prevention%2C36%2C44%2C1308%2C2560%2C720%2C2560%2C1440%2C1%2CL',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Referer': 'https://data.cdc.gov/NCHS/Provisional-Death-Counts-for-Coronavirus-Disease-C/hc4f-j6nb',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('accessType', 'DOWNLOAD'),
    )

    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    response.raise_for_status()
    return response.content


def dump_csv(csv_path, csv):
    with open(csv_path, "wb") as f:
        f.write(csv)

# import requests
#
# cookies = {
#     's_fid': '582F41E5B5EE3F91-06D2B37F363E3DB1',
#     '_ga': 'GA1.2.1330760792.1584017985',
#     '_socrata_session_id': 'BAh7CEkiD3Nlc3Npb25faWQGOgZFRkkiJTJmODQ1NzVkOTliMTkwYThlMGMyMjIzZDZlNzI3MjIyBjsARkkiCXVzZXIGOwBGMEkiEF9jc3JmX3Rva2VuBjsARkkiMUNUc2JQQmc2ZGRyVW1YN29lYU4zMnJWZHNHbk9zeHZyaitWZER3T1crOXM9BjsARg%3D%3D--0482c883277b0b57ac3ac777eedfbf4ca9195a0f',
#     '_gid': 'GA1.2.681595992.1587979645',
#     's_vnum': '1588280400166%26vn%3D4',
#     's_invisit': 'true',
#     's_lv_s': 'Less%20than%207%20days',
#     's_visit': '1',
#     's_cc': 'true',
#     '_gat_GSA_ENOR0': '1',
#     '_4c_': 'hVNNb6MwEP0rFYeeChjb2CZStUoCaVK1oQ1ZrbYXFMAp3lBAQKDZKv997UCalSrt5pI3w7w3H5750LqU59rIshl1mMUohITdaDt%2BqLXRh1aJRP212kjjDoVOHCMdsi3RccKZzhyGdUQRsDcwQbETaTfau9JyLOogx4E2sI43WlwOGh%2FavsqkVNo0ZT0yza7rjDiJjdeiNfM4rc28rWuzravKjItWJGHH%2BS47mFJ27PoTLwy8IFj4y3DhShWbwRm2PHtiex6aOZYOiAsniM4QQR5yJ5akxUXCZajlGNQg0m5%2BK4sBCcuqSPZxEzaHUoV0PLqqk538kPBWxDzsRNKk8gO0Cbh4Uy5e00aJYHxyl5UyDGhLoxN5UnQXJsDs4r0wAcDSvS7KteCKLQ0%2F8B6CAY7daY9m2V6CnxItp%2FN5sH7q3Yv817469Nh7WvVgWry97XPRHO724tSy8qVVkYu4N5bTxcr9lPNeTiM8ZV4%2FrIfUd1kRbbI532Sn%2BtXY14G7Ogt48x4F5SYX9RDx%2BPhjNchORNWkLt%2FyuKkHzsIPBpL%2FND%2FX6k99fyAvggHdF9HAeRG7TY%2Biqujq04RUJ2%2F86vRuhYp7EPn%2BXRqVzFZV5ynWolGtDys1OOQq9z6V%2BXG9CifeeOov%2F1pDFW9Z0IAFNXLemJEpt1A61Vpa5n2gQwMYwKxthm2Aqc0AAMT6Nn6e3FrXW5Hc%2FncTr8fP3q3ax1Jdknr9rIg3mSpWHp8c%2FDj8fnoQCyFACaAONORFYiDviNnacTgrxgChBNmUYLnKjTwlRjBQPxnRivOlwphCChnTHZ4AHdsbojuAYJ1sKYIJiaItwudLVVePgJREbJC02FmxzAZF6xLsYEBku%2FQcjD%2Fzl%2B0Qjb9UC79W279tKKf8D96XLo%2FHPw%3D%3D',
#     '_gat_socrataSiteChrome': '1',
#     'gpv_c54': 'https%3A%2F%2Fdata.cdc.gov%2FNCHS%2FProvisional-Death-Counts-for-Coronavirus-Disease-C%2Fpj7m-y5uh',
#     's_ppvl': 'Provisional%2520Death%2520Counts%2520for%2520Coronavirus%2520Disease%2520%2528COVID-19%2529%2520%257C%2520Data%2520%257C%2520Centers%2520for%2520Disease%2520Control%2520and%2520Prevention%2C55%2C72%2C6369%2C2560%2C720%2C2560%2C1440%2C1%2CL',
#     'gpv_v45': 'Provisional%20Death%20Counts%20for%20Coronavirus%20Disease%20%28COVID-19%29%3A%20Weekly%20State-Specific%20Data%20Updates%20%7C%20Data%20%7C%20Centers%20for%20Disease%20Control%20and%20Prevention',
#     'socrata-csrf-token': 'xYLAMq9bBL8TOgMLF5e74p1FKw73R4bN+HA4Z5Ye27bMudsOt2FxZcejfeNuNMw4KBibZzn0nSZ3lWVolYggbQ==',
#     's_ptc': '0.01%5E%5E0.00%5E%5E0.00%5E%5E0.00%5E%5E0.96%5E%5E0.90%5E%5E3.82%5E%5E0.01%5E%5E4.83',
#     's_ppv': 'Provisional%2520Death%2520Counts%2520for%2520Coronavirus%2520Disease%2520%2528COVID-19%2529%253A%2520Weekly%2520State-Specific%2520Data%2520Updates%2520%257C%2520Data%2520%257C%2520Centers%2520for%2520Disease%2520Control%2520and%2520Prevention%2C36%2C36%2C1255%2C2560%2C720%2C2560%2C1440%2C1%2CL',
#     's_lv': '1587981890328',
#     's_sq': '%5B%5BB%5D%5D',
#     's_tps': '16',
#     's_pvs': '24',
# }
#
# headers = {
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#     'Sec-Fetch-Dest': 'document',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Referer': 'https://data.cdc.gov/NCHS/Provisional-Death-Counts-for-Coronavirus-Disease-C/pj7m-y5uh',
#     'Accept-Language': 'en-US,en;q=0.9',
# }
#
# params = (
#     ('accessType', 'DOWNLOAD'),
# )
#
# response = requests.get('https://data.cdc.gov/api/views/pj7m-y5uh/rows.csv', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://data.cdc.gov/api/views/pj7m-y5uh/rows.csv?accessType=DOWNLOAD', headers=headers, cookies=cookies)

if __name__ == "__main__":
    "https://data.cdc.gov/api/views/hc4f-j6nb/rows.csv"
    csv_race = download_raw_data("https://data.cdc.gov/api/views/pj7m-y5uh/rows.csv")
    dump_csv("us_covid_provisional_race_data.csv", csv_race)