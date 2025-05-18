def analyze_word_frequency(top_n=10):
    """分析弹幕中的词频并生成词云图"""
    import jieba
    from collections import Counter
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties

    # 设置支持中文的字体
    font_path = 'simhei.ttf'  # 确保 simhei.ttf 存在于项目目录中
    font = FontProperties(fname=font_path)

    # 读取所有弹幕内容
    with open('danmu.log', 'r', encoding='utf-8') as f:
        texts = [line.split(': ')[-1].strip() for line in f if ': ' in line]

    # 中文分词
    words = []
    for text in texts:
        words.extend(list(jieba.cut(text)))  # 使用 jieba.cut 并转换为列表

    # 过滤短词和停用词
    filtered_words = [word for word in words if len(word) > 1 and not word.isspace()]

    # 统计词频
    word_counts = Counter(filtered_words)

    # 返回最高频的词语
    top_words = word_counts.most_common(top_n)

    # 生成词云图
    wordcloud = WordCloud(font_path=font_path, width=800, height=400,
                          background_color='white').generate_from_frequencies(word_counts)

    # 显示词云图
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('弹幕词云图', fontproperties=font)  # 使用支持中文的字体
    plt.show()

    # 保存词云图为图片文件
    wordcloud.to_file('wordcloud.png')

    return top_words

analyze_word_frequency()