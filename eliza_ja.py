from elizapack.eliza import eliza
from googletrans import Translator


class Eliza_ja(eliza):
    """eliza.eliza クラスの日本語対応版"""

    def respond_ja(self, inp_s):
        """日本語で入力を受け付けて日本語で返答する

        Returns:
            str: 日本語の返答
        """

        # googletrans を使って日本語で会話できる Eliza を作る
        translator = Translator()

        # 入力の日本語を英語へ変換
        translated = translator.translate(inp_s, src='ja', dest='en')
        inp_en_s = translated.text

        # Eliza に英語の入力を投げて英語の返答を受け取る
        reply = super().respond(inp_en_s)

        # 返答の英語を日本語へ変換
        translated = translator.translate(reply, src='en', dest='ja')
        reply_ja = translated.text
        return reply_ja


if __name__ == "__main__":
    # セラピストを生成する
    therapist = Eliza_ja()
    # 入力と回答
    print("イライザ:", therapist.respond_ja("こんちには"))
