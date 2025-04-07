# AIE6-S01 Homework

## 📚 Table of Contents

- [Activity #1](#activity-1)
- [Vibe Check Evaluation](#-vibe-check-evaluation)
- [Advanced Build](#advanced-build)
- [Additional Notes on Advanced Build Tasks](#additional-notes-on-advanced-build-tasks)
  - [Task 1: Model Update](#task-1-model-update)
  - [Task 2: Token Usage Tracking](#task-2-token-usage-tracking)
  - [Task 3: Prompt Router Implementation (PoC)](#task-3-prompt-router-implementation-poc)
- [Three Lessons Learned](#three-lessons-learned)
- [Three Lessons Not Yet Learned](#three-lessons-not-yet-learned)

## Activity #1

> Please evaluate your system on the following questions *(MLW Note: The Aspect Tested responses are in the __Vibe Check Evaluation__ table)*:
>
> 1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
> 1. Read the following paragraph and provide a concise summary of the key points…
> 1. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
> 1. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
> 1. Rewrite the following paragraph in a professional, formal tone…

### 👍👎 Vibe Check Evaluation

| # | Prompt Description                                                                 | Aspect Tested                        | Evaluation (1–5) | Notes / Observations                                                                 |
|---|------------------------------------------------------------------------------------|--------------------------------------| :---: |------------------------------------------------------------------------------------------------|
| 1 | Explain OOP to a complete beginner                                                 | Clarity & Response Tone              | 3+ | Comments: Content could still be difficult for a "... complete beginner”. The updated model response is better (a 4). ChatGPT 4o is a solid 4.9. *(Check out the PDF to see if you find the error it made — without that it would be a 5+!)*
 |
| 2 | Summarize a provided paragraph                                                     | Summarization                        | 2 | The output is too similar to the original paragraph. It basically reduced it by only 12 words (99 -> 87). The Updated Model did better (a 3+): an enumerated list; still wordy. My Prompt-Router version is a 4. The enhancement needs a wider range for summation points (2 to 5 instead of 2 or 3). |
| 3 | Write a short, imaginative story about a robot finding friendship                 | Creative Writing / Imaginative Task | 4 | It did a good job with this one (🤔 … I wonder if it would ever create a male ladybug in a story). The Updated Model gets a 4+ with a more engaging story.. Prompt-Router gets just under a 5: Much more engaging and vivid descriptions. *(The Prompt-Router did make a small error many will probably miss.)* |
| 4 | Determine packs of apples & oranges to meet exact quantities                      | Logic / Math Reasoning               | 4 | I expected this one to come up with the wrong answer until the prompt was enhanced with a CoT instruction -- something a teacher might plant so a student could fix it in the *Advanced Build* 😉. I found the CoT was already being added to the User Template. I ran a test without the CoT and it still responded correctly -- expectation squashed. Comparing the Original implementation with the Updated Model and Prompt-Router, I actually give the nod to the Original. While I appreciated the directness and brevity of the Prompt-Router, I would prefer the Original if I were being taught something new to me. |
| 5 | Rewrite a paragraph in a formal, professional tone                                 | Tone Shifting (Informal → Formal)    | 4 | The Original did what it was told to do and as a result, lost engagement. The Updated Model’s response was even more formal. The Prompt-Router managed to elevate the formality of the story while also being the most engaging. Looking at the prompt enhancements, I can see why. |



## Advanced Build:

>Please make adjustments to your application that you believe will improve the vibe check done above, push the changes to your HF Space and redo the above vibe check.
>
> > NOTE: You may reach for improving the model, changing the prompt, or any other method.

| Modification | Branch | Merged To Production? | Chat Logs |
|------------------------------|--------------------| :------: |------------------------------|
| Update the Model Used | [AIE6-S01_model-update](https://github.com/mwalker-tmd/Beyond-ChatGPT/tree/AIE6-S01_model-update) | ✅ | [Model Update Logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_model-update.md)
| Investigate Token Usage | [AIE6-S01_token-usage](https://github.com/mwalker-tmd/Beyond-ChatGPT/tree/AIE6-S01_token-usage) | ❌ | [Token Usage Logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_token-usage.md)
| *Proof of Concept:* Dynamic Prompt Enhancement | [AIE6-S01_prompt-router](https://github.com/mwalker-tmd/Beyond-ChatGPT/tree/AIE6-S01_prompt-router) | ✅ | [Dynamic Prompt Enhancement Logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_prompt-router.md)
| ChatGPT 4.0 Results | None | n/a | [ChatGPT 4.0 Question 1](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_chatgpt-4.md)


## Additional Notes on Advanced Build Tasks

## Task 1: Model Update
- Updated model selection in settings

### Code Changes
- Branch: `AIE6-S01_model-update`
- Files modified:
  - `app.py`: Updated model settings

### Testing Results
See the [chat logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_model-update.md)

## Task 2: Token Usage Tracking
- Added token counting for prompts and responses
- Implemented logging to both terminal and UI
- Used tiktoken for accurate token counting

### Code Changes
- Branch: `AIE6-S01_token-usage`
- Files modified:
  - `app.py`: Added token tracking
  - `pyproject.toml`: Added tiktoken dependency

### Testing Results
See the [chat logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_token-usage.md)

## Task 3: Prompt Router Implementation (PoC)
- Created a separate Python module for prompt analysis and enhancement
- Implemented basic task classification
- Added few-shot examples for tone conversion
- Limited Chain of Thought prompting to Math/Logic content (was being sent on every prompt) 
- Added logging for debugging

### Code Changes
- Branch: `AIE6-S01_prompt-router`
- Files modified:
  - `app.py`: Added integration with prompt router
  - `prompt_router.py`: New file for prompt analysis

### Testing Results
See the [chat logs](https://github.com/mwalker-tmd/Beyond-ChatGPT/blob/production/docs/2025-04-06_prompt-router.md)

### Next Steps

In a real world environment, if the proof of concept was approved the implementation would be improved by utilizing an LLM to:

- Determine the task type. This would likely involve:
  - Instructing it to pick from a list of types, including a default value if none of the other types applied
  - Using few-shot prompting to instruct it on what the task types values represent
- Provide the prompt enhancement(s) for the determined task type

## Three Lessons Learned
- Third Party Plugins: Check for versions to ensure you are looking at the correct documentation before making coding changes!
- The value of paired programming with an AI Coding Assistant! … And the need to watch over Claude and help him out from time to time!
- The educational benefits of discussing white papers with an AI (example: I had it generate practice suggestions for the key concepts).

## Three Lessons Not Yet Learned
Some things I want to dive deeper into as a result of this session:
- OpenAI API configuration options (which I will learn by diving into their documentation as instructed!)
- How to unit test functions (for example, the new functions in python_router.py)
- How Cursor’s debugger works
