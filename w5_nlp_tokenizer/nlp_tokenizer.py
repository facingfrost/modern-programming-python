import jieba
from matplotlib import pyplot as plt

class Tokenizer:
    def __init__(self, strings, coding, PAD):
        self.chars = strings
        if coding == "c":
            self.coding = "c"
            word_list=list(set(list("".join(strings))))
        else:
            self.coding = "w"
            word_list=list(set(jieba.lcut("".join(strings))))
        order = [i for i in range(1,len(word_list)+1)]
        self.dictionary = dict(zip(word_list, order))
        self.dictionary["PAD"] = 0

    def tokenize(self,sentence):
        if self.coding == "c":
            list_of_chars = list(sentence)
        else:
            list_of_chars = jieba.lcut(sentence)
        return list_of_chars

    def encode(self,list_of_chars):
        tokens = []
        for i in list_of_chars:
            tokens.append(self.dictionary[i])
        return tokens

    def trim(self,tokens,seq_len):
        delta = seq_len-len(tokens)
        if delta > 0:
            for i in range(delta):
                tokens.append(0)
        return tokens

    def decode(self,tokens):
        new_dict = {v : k for k, v in self.dictionary.items()}
        sentence_list = []
        for i in tokens:
            sentence_list.append(new_dict[i])
        return sentence_list

    def encode_all(self,seq_len):
        all_tokens = []
        if self.coding == "c":
            for i in self.chars:
                if len(list(i)) == seq_len:
                    all_tokens.append(self.encode(self.tokenize(i)))
        else:
            for i in self.chars:
                if len(jieba.lcut(i)) == seq_len:
                    all_tokens.append(self.encode(self.tokenize(i)))
        return all_tokens




if __name__ == "__main__":
    sentence_list = []
    with open('./jd_comments.txt', 'r',encoding='utf-8') as f:
        for line in f.readlines():
            sentence_list.append(line.strip())
    tokenizer = Tokenizer(sentence_list, "c", 0)
    len_list = []
    for i in tokenizer.chars:
        len_list.append(len(tokenizer.encode(tokenizer.tokenize(i))))
    len_list = sorted(len_list)
    frequency_dict = {}
    for i in len_list:
        frequency_dict[i] = frequency_dict.get(i,0) + 1
    x = list(frequency_dict.keys())
    y = list(frequency_dict.values())
    plt.plot(x,y)
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()

