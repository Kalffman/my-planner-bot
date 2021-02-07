import os

properties = {
    "BOT_TOKEN": os.environ["BOT_TOKEN"],
    "PLANNER_API": f"http://{os.environ['PLANNER_API_HOST']}:{os.environ['PLANNER_API_PORT']}",
}
