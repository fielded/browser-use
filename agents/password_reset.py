import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
import traceback
from dotenv import load_dotenv
from helpers.loaders import load_task_list_from_yaml
from helpers.error_util import log_error_to_markdown

load_dotenv()

async def run_agent(browser: Browser, browser_context):
    try:
        # Load tasks
        reset_data = load_task_list_from_yaml("tasks/SL/password_reset.yaml")

        if not isinstance(reset_data, dict) or "tests" not in reset_data:
            raise ValueError("password_reset.yaml must contain a 'tests' key with a list of steps.")

        reset_tasks = reset_data["tests"]

        # Build full task text
        full_task = " ".join([t["task"] for t in reset_tasks])
        print("\nRunning full task:\n", full_task)

        # Run the agent
        llm = ChatOpenAI(model="gpt-4o")
        agent = Agent(
            task=full_task,
            llm=llm,
            browser=browser,
            browser_context=browser_context,
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
                        soft_fail_terms = [
                            "dns", "shared email", "not resolved", "error",
                            "invalid email format", "rate limit", "failed",
                            "does not allow"
                        ]
                        if any(term in text for term in soft_fail_terms):
                            log_error_to_markdown(
                                error=res.extracted_content,
                                context="⚠️ Issue with password reset",  # check on steps completed.
                                filename="soft_failures.md"
                            )
                            print("⚠️ Soft failure logged.")

    except Exception as e:
        # Hard failure logging
        error_message = f"{str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        log_error_to_markdown(
            error=error_message,
            context="💥 Unhandled exception during agent run",
            filename="hard_failures.md"
        )
        print("🛑 Exception occurred and was logged.")

    finally:
        print("Password reset agent done")
