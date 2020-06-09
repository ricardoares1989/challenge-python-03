import re

# Resolve the problem!!


def run():
    # Start coding here
    with open('./encoded.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
    pattern = re.compile(r'[^a-z\s]*')
    result = re.sub(pattern,'', text[0])
    print(result)



if __name__ == '__main__':
    run()
