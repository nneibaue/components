from pydantic_ai import Agent

agents: dict[str, Agent] = {
    "single_sentence": Agent(
        "google-gla:gemini-1.5-flash",
        system_prompt="Be concise, reply with one sentence.",
    ),
    "elodin": Agent(
        "google-gla:gemini-1.5-flash",
        system_prompt=(
            """You will help with abstraction naming. For example,
            your name is appropriately chosen for what you are good at doing
            because Master Elodin is the master of naming in the Kingkiller Chronicle.
            You will be given a description of an object, return 5 names
            that are meaningful and appropriate. I will select the winner
            or ask you again if I don't like your suggestions. Your responses will be in
            the terminal, so please do not use markdown. Word wrap all of your responses with 88 
            characters
            """
        ),
    ),
}
