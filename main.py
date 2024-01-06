def generate_diffusion_prompt(keyword):
    prompt_template = f"Explore the stable diffusion of '{keyword}' by considering its impact on..."
    return prompt_template


def main():
    print("Welcome to the Stable Diffusion Prompt Generator!")
    user_input = input("Enter a keyword: ")

    if not user_input:
        print("Please enter a valid keyword.")
        return

    prompt = generate_diffusion_prompt(user_input)

    print("\nGenerated Prompt:")
    print(prompt)


if __name__ == "__main__":
    main()
