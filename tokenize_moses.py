from sacremoses import MosesTokenizer, MosesDetokenizer

mt = MosesTokenizer(lang='ro')
with open('ro') as in_file:
    with open('ro.tok','w') as out_file:
        for line in in_file:
            tokenized_line = mt.tokenize(line,return_str=True)
            out_file.write(tokenized_line)
            out_file.write('\n')


