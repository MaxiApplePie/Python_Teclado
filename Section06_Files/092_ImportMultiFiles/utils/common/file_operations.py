def save_to_file(content, filename):
    fp = open(filename, 'w')
    fp.write(content)
    fp.close()


def read_file(filename):
    fp = open(filename, 'r')
    content = fp.read()
    fp.close()
    return content
