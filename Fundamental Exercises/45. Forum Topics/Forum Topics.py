forum_dict = {}
while True:
    data = input()
    if data == "filter":
        break
    else:
        topic = data.split(' -> ')[0]
        tags = data.split(' -> ')[1].split(', ')
        if topic in forum_dict.keys():
            forum_dict[topic].extend(tags)
        else:
            forum_dict[topic] = tags
tags_required = input().split(', ')
for k, v in forum_dict.items():
    unique_tags_list = sorted(set(v), key=v.index)
    forum_dict[k] = unique_tags_list
    tags_required_set = set(tags_required)
    if tags_required_set.issubset(v):
        unique_tags_list = ["#" + i for i in unique_tags_list]
        print(f'{k} | {", ".join(unique_tags_list)}')

"""
HelloWorld -> hello, forum, topic
HelpWithHomework -> homework, forum, topic
AnotherHelp -> headstart
filter
forum, topic
"""