import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup-ALICE.xml")
kernel.respond("load aiml b")
kernel.saveBrain("bot_brain_ALICE.brn")