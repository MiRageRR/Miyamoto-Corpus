import numpy as np
from collections import Counter

def extract_trigrams(text):
    # 連続する三文字の組み合わせ（トリグラム）を抽出
    trigrams = [text[i:i+3] for i in range(len(text) - 2)]
    return trigrams

def extract_bigrams(text):
    # 連続する二文字の組み合わせ（バイグラム）を抽出
    bigrams = [text[i:i+2] for i in range(len(text) - 1)]
    return bigrams

def count_unique_trigrams(trigrams):
    # トリグラムの種類を数え上げる
    unique_trigrams = set(trigrams)
    return len(unique_trigrams)

def count_unique_bigrams(bigrams):
    unique_bigrams = set(bigrams)
    return len(unique_bigrams)

def calculate_entropy(corpus, M):
    ngram_counts = Counter(corpus)
    total_ngrams = sum(ngram_counts.values())

    # 各バイグラムまたはトリグラムの確率を計算
    ngram_probabilities = {ngram: count/total_ngrams for ngram, count in ngram_counts.items()}

    # エントロピーを計算
    entropy = -sum(prob * np.log2(prob) for prob in ngram_probabilities.values())

    # 拡張エントロピーを計算
    extended_entropy = M * entropy

    return extended_entropy

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
    
    return unique_trigram_count, unique_bigram_count, all_bigrams, all_trigrams

def main():
    # テスト用のIPA表記の文
    ipa_text = input("Enter IPA text: ")

    # 空白でセグメントした後にトリグラムとバイグラムをカウント
    unique_trigram_count, unique_bigram_count, all_bigrams, all_trigrams = process_text_by_segments(ipa_text)

    print("Unique Trigram Count:", unique_trigram_count)
    print("Unique Bigram Count:", unique_bigram_count)
    
    # バイグラムのエントロピーを計算
    bigram_entropy = calculate_entropy(all_bigrams, 2)  # M=2
    print(f"Bigram Entropy: {bigram_entropy}")

    # トリグラムのエントロピーを計算
    trigram_entropy = calculate_entropy(all_trigrams, 3)  # M=3
    print(f"Trigram Entropy: {trigram_entropy}")

if __name__ == "__main__":
    main()
