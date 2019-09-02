import re

websites = []
class Websites:

    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        if queries is None:
            queries = []
        self.queries = queries

data = input()
while not data == "end":
    input_host = data.split(' | ')[0]
    input_domain = data.split(' | ')[1]
    if "," in data:
        input_queries = re.split(' | |,', data)[4:]
        website = Websites(input_host, input_domain, input_queries)
        websites.append(website)
    else:
        website = Websites(input_host, input_domain)
        websites.append(website)

    data = input()
for website in websites:
    input_host = website.host
    input_domain = website.domain
    input_queries = website.queries
    string_query = ""
    for query in input_queries:
        if len(input_queries) > 0:
            string_query += f"[{query}]&"
    if len(string_query) > 0:
        string_query = string_query[:-1]
        print(f'https://www.{input_host}.{input_domain}/query?={string_query}')
    else:
        print(f'https://www.{input_host}.{input_domain}')

""""
https://www.{host}.{domain}/query?=[{query1]&amp;[{query2}]&amp;[query3].
softuni | bg | user,course,homework
judge.softuni | bg | contest,bg
google | bg | search,query
zamunda | net
"""