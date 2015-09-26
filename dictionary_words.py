if __name__ == '__main__':
    print("hi there")
    with open('/usr/share/dict/words', encoding='utf-8') as the_file:
        a_string = the_file.readlines()
        print(a_string)
        # print(a_string[:20])
        # if the_file.closed:
        #     the_file.close()
