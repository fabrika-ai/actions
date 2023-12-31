# Extend ChatGPT with Community Actions

Do you have a GPT Assistant? Would you like it to do more? 

# About
Welcome to our project where we empower ChatGPT with Community Actions! This is an open invitation for developers like you to contribute and enrich ChatGPT's capabilities. 

Join us in building an extensive, dynamic, and diverse set of actions that ChatGPT can perform.

## What is an Action?
Action is a way for GPT to perform various tasks or functions beyond standard text generation. It’s a way to extend the utility of ChatGPT. 

## What could be an Action?
Anyhing! 'Generate Image' is an Action, 'Calculate square root of 4' is an action, and so is 'Send my mom a text'.

## How does it work?
You can use any Actions from this repo, you can also create a new one. We are hosting your actions and make integration to GPT Assistants seemless.

# Getting started
## How to Run an action from "Community Actions"
1. Decide what actions you plan to use in your GPT.
2. Go to [GPT Editor](https://chat.openai.com/gpts/editor) -> Configure -> Scroll to the very bottom -> Click `Add actions` -> Click `Import from URL`.
3. Paste `https://actions.tryfabrika.com/combine?actions=<ACTIONS>`, where `<ACTIONS>` is a list of action separated with `,`:
   - Examples:
     - Single action: `https://actions.tryfabrika.com/combine?actions=yfinance`
     - Multiple actions: `https://actions.tryfabrika.com/combine?actions=template,yfinance`
4. Go to Authentification -> Click on `Settings` -> Select `API Key` -> Insert your API key -> Select `Bearer` at `Auth Type`.

Congrats! Your actions are ready to be used by ChatGPT!

# Setup
## How to Create your own Custom GPT Actions?

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


## API key access 

We are in a private.beta, if you would like to get API key for testing please sign up to a waitlist: https://forms.gle/V18giB3upYiG7ARq8


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
