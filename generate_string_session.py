from pyrogram import Client as c

API_ID = input("\7420144:\n > ")
API_HASH = input("\n6c6db1723e77bf0ec27f27b30eb699d7:\n > ")

print("\n\n 918092431240.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
