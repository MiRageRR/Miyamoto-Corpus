def extract_trigrams(text):
    # 連続する三文字の組み合わせ（トリグラム）を抽出
    trigrams = [text[i:i+3] for i in range(len(text) - 2)]
    return trigrams

def count_unique_trigrams(trigrams):
    # トリグラムの種類を数え上げる
    unique_trigrams = set(trigrams) # セットにすることで重複を排除
    return len(unique_trigrams)

def extract_bigrams(text):
    # 連続する二文字の組み合わせ（バイグラム）を抽出
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    return bigrams

def count_unique_bigrams(bigrams):
    unique_bigrams = set(bigrams) # セットにすることで重複を排除
    return len(unique_bigrams)

def process_text_by_segments(text):
    # 空白で文章を分割
    segments = text.split()
    all_trigrams = []
    all_bigrams = []

    for segment in segments:
        # 各セグメントについてトリグラムとバイグラムを抽出
        trigrams = extract_trigrams(segment)
        bigrams = extract_bigrams(segment)
        all_trigrams.extend(trigrams)
        all_bigrams.extend(bigrams)

    # ユニークなトリグラムとバイグラムの数をカウント
    unique_trigram_count = count_unique_trigrams(all_trigrams)
    unique_bigram_count = count_unique_bigrams(all_bigrams)
    
    return unique_trigram_count, unique_bigram_count

# テスト用のIPA表記の文
ipa_text = input("Enter IPA text: ")

# 空白でセグメントした後にトリグラムとバイグラムをカウント
unique_trigram_count, unique_bigram_count = process_text_by_segments(ipa_text)

print("Unique Trigram Count:", unique_trigram_count)
print("Unique Bigram Count:", unique_bigram_count)
