import random
from flask import Flask, render_template, request

app = Flask(__name__)

reasons = [
    "宇宙線の影響",
    "CPUの熱暴走",
    "重力が強い",
    "月の引力",
    "猫の気配",
    "Wi-Fiの機嫌"
]

advice = [
    "5分だけ始めよう！",
    "まずPCを開くだけでもOK！",
    "タイマーを3分セット！",
    "未来の自分が喜ぶよ！"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        task = request.form["task"]

        result = {
            "task": task,
            "reason": random.choice(reasons),
            "score": random.randint(1, 99),
            "advice": random.choice(advice)
        }

    return render_template("index.html", result=result)

app.run(host="0.0.0.0", port=5000)
