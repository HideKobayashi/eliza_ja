# eliza_ja
Eliza in Japanese with Python（日本語版の Eliza / Python）

## これは何？

このソフトウエアは、Jez Higgins 氏によって GitHub に公開された eliza.py というソフトウエアを日本語化したものです。日本語化するにあたっては、今回はgoogletrans を利用しています。googletrans は Google が Web サービスとして提供している翻訳サービスを Python から使えるようにするためのライブラリです。

### 環境構築

このリポジトリに置いてあるファイルが配置されたディレクトリの下に、elizapack というディレクトリを作り、そこに オリジナルのJez Higgins 氏のリポジトリからダウンロードした eliza.py を配置してください。

    eliza.py, Eliza in Python by Jez Higgins et. al.
    https://github.com/HideKobayashi/eliza.py

googletrans を PyPI からインストールします。

    pip install googletrans

### 実行方法

ターミナルで run_eliza_ja.py を実行してください。

    python run_eliza_ja.py

以上です。
