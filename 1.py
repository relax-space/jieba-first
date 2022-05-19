'''
说明: 主要是理解步骤
1. 准备: 
    去掉停用词
    将分词合并: 增加自定义分词: 我/爱 ==> 我爱
    将分词分开: suggest_freq: 北京 => 北/京
2. 正常分词
'''
import jieba


def get_stopwords():
    with open('stopword.txt', mode='r', encoding='utf8') as f:
        return [i.strip() for i in f.readlines()]


def s1():
    # 1. 正常分词
    s1 = '我爱北京天安门'
    words = jieba.lcut(s1)
    assert '我/爱/北京/天安门' == '/'.join(words), 'jb1 1 error'

    # 2. 停用词
    stops = get_stopwords()
    stops.extend(['北京', '门'])
    new_words = [i for i in words if i not in stops]
    assert '爱/天安门' == '/'.join(new_words), 'jb1 2 error'

    # 3. 增加分词
    jieba.add_word('我爱')
    words = jieba.lcut(s1)
    assert '我爱/北京/天安门' == '/'.join(words), 'jb1 3 error'

    # 4. 自定义频率
    jieba.suggest_freq(('北', '京'), True)
    words = jieba.cut(s1, HMM=False)
    assert '我爱/北/京/天安门' == '/'.join(words), 'jb1 4 error'


def main():
    s1()


if __name__ == '__main__':
    main()
