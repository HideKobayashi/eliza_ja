from eliza_ja import Eliza_ja

# セラピストを生成する
therapist = Eliza_ja()

# 最初のメッセージ
print("イライザに何か日本語で話してください。")
print("やめるときは やめる または さようなら と入力してください。")

while True:
    inp_s = input("あなた: ")
    if inp_s == "":
        continue
    if inp_s == "やめる" or inp_s == "さようなら":
        print("イライザ: さようなら")
        break
    reply_ja = therapist.respond_ja(inp_s)
    print("イライザ: {}".format(reply_ja))
