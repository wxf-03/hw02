from openai import OpenAI

# API 配置
client = OpenAI(
    api_key="sk-af4d43fde89d42e48918da0d5fa6896c",
    base_url="https://api.deepseek.com/v1"
)

# 聊天主程序
print("===== DeepSeek Chatbot =====")

while True:
    user_input = input("\nPlease input your question: ")

    # 退出程序
    if user_input.strip().lower() == "q":
        print("Program exit.")
        break

    # 空输入判断
    if not user_input.strip():
        print("Please enter valid content!")
        continue

    # 请求AI
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message.content
        print("\nAI:", answer)
    except Exception as e:
        print("\nRequest error:", e)
