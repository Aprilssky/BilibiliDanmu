def analyze_word_frequency(self, top_n=10):
    """分析弹幕中的词频"""
    import jieba
    from collections import Counter
    
    # 读取所有弹幕内容
    with open('danmu.log', 'r', encoding='utf-8') as f:
        texts = [line.split(': ')[-1].strip() for line in f if ': ' in line]
    
    # 中文分词
    words = []
    for text in texts:
        words.extend(jieba.lcut(text))
    
    # 过滤短词和停用词
    filtered_words = [word for word in words if len(word) > 1 and not word.isspace()]
    
    # 统计词频
    word_counts = Counter(filtered_words)
    
    # 返回最高频的词语
    return word_counts.most_common(top_n)
