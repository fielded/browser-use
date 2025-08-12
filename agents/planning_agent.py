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
        # topup_data = load_task_list_from_yaml("tasks/topup_plan.yaml")
        resupply_data = load_task_list_from_yaml("tasks/SL/resupply_plan.yaml")

        if not isinstance(resupply_data, dict) or "tests" not in resupply_data:
            raise ValueError("resupply_plan.yaml must contain a 'tests' key with a list of steps.")

        resupply_tasks = resupply_data["tests"]
        # topup_tasks = topup_data["tests"]

        # Build full task text
        full_task = " ".join([t["task"] for t in resupply_tasks])
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
                            "dns", "cannot be reached", "not resolved", "error",
                            "reset quantities",
                            "0 shipments"
                        ]
                        if any(term in text for term in soft_fail_terms):
                            log_error_to_markdown(
                                error=res.extracted_content,
                                context="⚠️ Issue with planning",  # check on steps completed.
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
        print("Planning agent done")
