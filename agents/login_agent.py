import asyncio
import os
import traceback
from browser_use import Browser, Agent
from langchain_openai import ChatOpenAI
from helpers.loaders import load_task_list_from_yaml
from helpers.error_util import log_error_to_markdown

async def run_agent(browser: Browser, browser_context):
    try:
        login_data = load_task_list_from_yaml("tasks/SL/login.yaml")
        nav_data = load_task_list_from_yaml("tasks/SL/navigation.yaml")

        if not isinstance(login_data, dict) or "tests" not in login_data:
            raise ValueError("login.yaml must contain a 'tests' key with a list of steps.")
        if not isinstance(nav_data, dict) or "tests" not in nav_data:
            raise ValueError("navigation.yaml must contain a 'tests' key with a list of steps.")

        login_tasks = login_data["tests"]
        nav_tasks = nav_data["tests"]
        full_task = " ".join([t["task"] for t in login_tasks + nav_tasks])

        # Run the agent
        llm = ChatOpenAI(model="gpt-4.1")
        agent = Agent(task=full_task, llm=llm, browser=browser, browser_context=browser_context)
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
                            "login failed", "incorrect username", "incorrect password",
                            "valid credentials are required"
                        ]
                        if any(term in text for term in soft_fail_terms):
                            log_error_to_markdown(
                                error=res.extracted_content,
                                context="⚠️ Issue with login / navigation ", #check on steps completed.
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
        print("Login agent finished (browser still active).")
