from agno.run import RunConfig
from app.agents.team import team


def route(question: str):
    return team.run_sync(
        question,
        run_config=RunConfig(
            reasoning=True,
            search_knowledge=True,
            reflexion=True
        )
    )
