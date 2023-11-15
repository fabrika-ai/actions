# Extend ChatGPT with Community Actions

Welcome to our project where we empower ChatGPT with custom community actions! This is an open invitation for developers like you to contribute and enrich ChatGPT's capabilities. Join us in building an extensive, dynamic, and diverse set of actions that ChatGPT can perform.

## About This Project

We've developed a way to seamlessly integrate custom actions into ChatGPT using FastAPI. This allows ChatGPT to perform a wide range of functions, from fetching stock data to generating graphs, and even interacting with external APIs. Our goal is to expand ChatGPT's utility and make it a more versatile tool for users across various domains.

## API key access 

We are in a private.beta, if you would like to get API key for testing please sign up to a waitlist: https://forms.gle/V18giB3upYiG7ARq8

## How to Run an action from "Community Actions"

1. Decide what actions you plan to use in your GPT.
2. Go to [GPT Editor](https://chat.openai.com/gpts/editor) -> Configure -> Scroll to the very bottom -> Add action -> Click `Import from URL`
3. Paste `https://actions.tryfabrika.com/combine?actions=<ACTIONS>`, where `<ACTIONS>` is a list of action separated with `,`:
   - Examples:
     - Single action: `https://actions.tryfabrika.com/combine?actions=yfinance`
     - Multiple actions: `https://actions.tryfabrika.com/combine?actions=template,yfinance`
4. Go to Authentification -> Click on `Edit` -> Select `API Key` -> Insert your API key -> Select `Bearer` at `Auth Type`

Congrats! Your action is ready to be used by ChatGPT!

## How to Create your own "Community actions"?

Your community actions can make a significant difference! Here’s how you can get involved:

- **Fork the Repository**: Start by forking this repository to your GitHub account.
- **Create Your Action**: Develop your custom action using FastAPI. Check out our existing examples for inspiration.
  - Duplicate `template` folder
  - Rename it to `<YOUR ACTION NAME>`
  - Edit `main.py` to create your actions
  - Edit `test_<YOUR ACTION>` and add relevant unit tests 
- **Test Your Code**: Ensure your action works as expected. We love robust and reliable contributions!
- **Document Your Action**: Write clear and concise documentation for your action. This should include its purpose, how it works, and any necessary parameters.
- **Submit a Pull Request**: Once your action is ready and documented, submit a pull request to our repository.

## Guidelines for Contribution

- **Code Quality**: Write clean, efficient, and well-commented code.
- **Functionality**: Your action should perform a useful task that enhances ChatGPT's abilities.
- **Originality**: We welcome unique and innovative ideas. Make sure your action adds value in a way not already covered by existing actions.
- **Security**: Ensure your action does not compromise the security or privacy of users.

## Why Contribute?

- **Innovate**: Be a part of something cutting-edge and contribute to the AI community.
- **Collaborate**: Work with other talented developers and learn from their insights.
- **Recognition**: Get credit for your work and showcase your skills to a broad audience.
- **Impact**: Help make ChatGPT more useful for a diverse range of applications.

## Need Help?
Got questions or need help getting started? Feel free to raise an issue in the repository or contact us directly.
