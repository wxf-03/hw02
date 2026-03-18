from openai import OpenAI
import os

# 初始化AI客户端
client = OpenAI(
    api_key="sk-test-homework-key",
    base_url="https://api.deepseek.com/v1"
)

def simple_chat():
    """功能1：简单对话"""
    print("\n===== Simple Chat Mode =====")
    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "q":
            print("Exit chat mode.")
            break
        if not user_input.strip():
            print("Please input valid content!")
            continue
        
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": user_input}]
            )
            print("AI:", response.choices[0].message.content)
        except Exception as e:
            print("Error:", e)

def paper_guide():
    """功能2：论文导读（作业必须项）"""
    print("\n===== Paper Guide Mode =====")
    print("Please input paper content:")
    
    paper_text = input("\nPaper: ")
    
    prompt = f"""
    You are an academic assistant.
    Please interpret this academic content:
    {paper_text}
    
    Please output:
    1. Core theme
    2. Key points
    3. Innovation
    4. Conclusion
    """
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        print("\n=== Interpretation ===")
        print(response.choices[0].message.content)
    except Exception as e:
        print("Error:", e)

def main():
    print("===== AI Chatbot Homework =====")
    print("1. Simple Chat")
    print("2. Paper Guide")
    print("q. Exit")
    
    choice = input("\nPlease choose: ")
    if choice == "1":
        simple_chat()
    elif choice == "2":
        paper_guide()
    elif choice == "q":
        print("Program exit.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
