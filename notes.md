
EMI lang tutor (formally EMIV5)
language tutor chatbot with async messaging and model agnostic behaviors,
following a defined curriculum and grading system to tutor users to their target language
and meet their individual learning needs.

interatcions
ideally interactions will be proxied through a microservice to save on monolith complexity, but for now will just be ran through a discord thread or service
(interactions is spawned as a process by the main application and communicated with via pipe)


contextualization
context will be built using the blocks approach with 2 fixed window size(s) depending on server performance (4k OR 8k)
chat memory context is scoped to include user messages in *all contexts (out of scope messages marketed)
and scoped messages from the specific channel, non-target user messages CANNOT be viewed out of scope by emi

example block

max_ctx=4,196 #2**12
ctx=[

]





:::CONFIG NOTES:::
default-heartbeat = f0.3s