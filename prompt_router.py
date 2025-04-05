import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
TONE_EXAMPLES = {
    "informal": "hey, can u help me with this?",
    "formal": "Hello, would you be able to assist me with this request?"
}

def classify_task(user_input: str) -> str:
    """Naive keyword-based classifier (can be replaced with LLM or ML later).
    
    NOTE: This is a naive implementation. It was coded with full knowledge of the specific prompts that will be used.
    For a production environment, this function would be modified to make a call to an LLM which would select the 
    most appropriate task type based on the user's input.
    """
    lowered = user_input.lower()
    if any(kw in lowered for kw in ["how many", "solve", "math", "packs"]):
        return "logic"
    elif any(kw in lowered for kw in ["rewrite", "make it formal", "tone"]):
        return "tone-formal"
    elif any(kw in lowered for kw in ["summarize", "key points", "main ideas"]):
        return "summary"
    elif any(kw in lowered for kw in ["story", "imaginative", "creative"]):
        return "story"
    else:
        return "default"

def build_enhanced_prompt(task_type: str, user_input: str) -> str:
    """Builds task-specific prompts, optionally with CoT or few-shot.
    
    NOTE: This is a naive implementation. It was coded with full knowledge of the specific prompts that will be used.
    For a production environment,this function would be modified to make a call to an LLM which would generate the
    appropriate prompt enhancements based on the user's input.
    """
    if task_type == "logic":
        return f"Let's solve this step by step.\n\n{user_input}"
    
    elif task_type == "summary":
        return f"Please summarize the following paragraph in 2-3 concise bullet points:\n\n{user_input}"

    elif task_type in ["tone-informal", "tone-formal"]:
        target_tone = "informal" if task_type == "tone-informal" else "formal"
        source_tone = "formal" if target_tone == "informal" else "informal"
        
        few_shot = (
            f"{source_tone.title()}: {TONE_EXAMPLES[source_tone]}\n"
            f"{target_tone.title()}: {TONE_EXAMPLES[target_tone]}\n\n"
            f"{source_tone.title()}: {user_input}\n"
            f"{target_tone.title()}:"
        )
        return few_shot
    
    elif task_type == "story":
        return (
            f"{user_input}\n\nMake it emotionally engaging and use vivid descriptions."
        )

    else:
        return user_input  # fallback to raw input

async def analyze_and_enhance_prompt(user_message: str) -> str:
    """
    Analyzes the user's message and enhances it with additional context or prefixes
    based on the content and intent of the message.
    
    Args:
        user_message (str): The original message from the user
        
    Returns:
        str: The enhanced message with additional context
    """
    task_type = classify_task(user_message)
    logger.info(f"Task type: {task_type}")
    enhanced_prompt = build_enhanced_prompt(task_type, user_message)
        
    return enhanced_prompt