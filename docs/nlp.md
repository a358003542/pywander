## nlp
some nlp tools

### auto_summary
将一篇文章按照句子或者段落分开，然后进行tf-idf评分。

word(tf) = Cword(target word count in sent)/C(all word count in sent)

word(idf) = log(C(sent count)/C(target word in sent count))

最后得出的摘要会按照原文顺序输出，只是选择性地将某些不重要的句子删除，你可以通过 max_len 来控制想要的摘要长度。


```
def auto_summary(content, word_tokenizer=None, sent_tokenizer=None,
                 stop_words=None, max_len=50):
```