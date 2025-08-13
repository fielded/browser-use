
from datetime import datetime
from browser_use.llm import ChatOpenAI
from browser_use import Agent
import traceback
from dotenv import load_dotenv

from helpers.loaders import load_task_list_from_yaml
from helpers.error_util import log_error_to_markdown
from helpers.extensions import system_prompt_extension

load_dotenv()

# Soft failure keywords for  tasks
soft_fail_terms = [
    "0 shipments",
    "cannot be reached",
    "cannot download",
    "cannot submit",
    "does not allow",
    "dns",
    "error",
    "failed",
    "incorrect password",
    "incorrect username",
    "invalid email format",
    "login failed",
    "not resolved",
    "operation failed",
    "reset quantities",
    "unable to proceed",
    "valid credentials are required"
]



# Function to run an agent with a given browser session and tasks
async def run_agent(browser_session, tasks, feature):
    print(f"=== Running {feature} agent ===")
    try:
        # Load tasks
        task_data = load_task_list_from_yaml(tasks)

        # Run the agent
        llm = ChatOpenAI(model="gpt-5-mini", temperature=0.1)
        agent = Agent(
            task=task_data,
            llm=llm,
            browser_session=browser_session,
            vision_detail_level='high',
            max_actions_per_step=3,
            system_prompt_extension=system_prompt_extension  # Add this instruction

        )
        await agent.run()

        # Soft failure
        if hasattr(agent, "state") and hasattr(agent.state, "last_result"):
            results = agent.state.last_result
            if isinstance(results, list):
                for res in results:
                    if hasattr(res, "extracted_content") and isinstance(res.extracted_content, str):
                        text = res.extracted_content.lower()

                        # Match soft failure keywords
                        if any(term in text for term in soft_fail_terms):
                            log_error_to_markdown(
                                error=res.extracted_content,
                                context=f"⚠️ Issue with {feature}",  # check on steps completed.
                                filename="soft_failures.md"
                            )
                            print("⚠️ Soft failure logged.")

    except Exception as e:
        print(f"🛑 Exception occurred in {feature} agent: {str(e)}")
        # Hard failure logging
        error_message = f"{str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        log_error_to_markdown(
            error=error_message,
            context="💥 Unhandled exception during agent run",
            filename="hard_failures.md"
        )
        print("🛑 Exception occurred and was logged.")

    finally:
        print(f"{feature} agent done")
