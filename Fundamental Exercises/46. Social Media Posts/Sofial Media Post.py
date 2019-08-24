social_dict = {}

while True:
    line = input()
    if line == "drop the media":
        break
    else:
        command = line.split()[0]
        post_name = line.split()[1]
        if command == "post":
            social_dict[post_name] = {'likes': 0, 'dislikes': 0, 'comments': []}
        elif command == "like":
            if post_name in social_dict.keys():
                social_dict[post_name]['likes'] += 1
        elif command == "dislike":
            if post_name in social_dict.keys():
                social_dict[post_name]['dislikes'] += 1
        else:
            if post_name in social_dict.keys():
                comm_name = line.split()[2]
                content = line.split()[3:]
                comment = {comm_name: content}
                social_dict[post_name]['comments'].append(comment)
for k, v in social_dict.items():
    print(f'Post: {k} | Likes: {v["likes"]} | Dislikes: {v["dislikes"]}')
    print("Comments:")
    if not v["comments"]:
        print("None")
    else:
        for i in v["comments"]:
            for k, v in i.items():
                print(f'*  {k}: {" ".join(v)}')
"""
post FirstPost
like FirstPost
like FirstPost
dislike FirstPost
post SecondPost
comment FirstPost Isacc Cool
comment SecondPost Isacc Lol
like SecondPost
drop the media
"""