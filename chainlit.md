![TAMARK Designs](./public/logo_light_transparent.png)

## Beyond ChatGPT 

This Chainlit app was created following instructions from [this repository!](https://github.com/AI-Maker-Space/Beyond-ChatGPT)

#### 🔧 Updates

- **Upgraded Model**: Switched from `gpt-3.5-turbo` to `gpt-4` for improved reasoning, tone control, and response quality.
- **Implemented Prompt Enhancer (Proof of Concept)**:  
  Introduced a backend component that programmatically augments user prompts based on task type. This enhancement adds strategies like:
  - **Few-Shot prompting** for tone and rewriting tasks
  - **Chain-of-Thought prompting** for logic and math problems  

  The system currently uses lightweight keyword-based classification to determine the task and apply the appropriate enhancement. The next phase would use an LLM to determine the task type.
