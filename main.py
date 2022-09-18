from pypresence import Presence
import time

start = int(time.time())
client_id = ""
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image="pepejam",
        large_text="AliDice Song",
        details="Thinking...",
        state="AliDice Song",
        start=start,
        buttons=[
            {"label": "StepBros", "url": "https://discord.gg/H6Dn3ZEhXH"},
            {"label": "Song", "url": "https://www.youtube.com/watch?v=xfr64zoBTAQ"}
        ]
    )
    time.sleep(60)