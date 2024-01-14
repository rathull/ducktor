# IDEA Hacks 2024 Server
# Inspiration

Due to doctor burnout and biases, especially post COVID-19, patients may not always be receiving optimal care when they visit doctors. Additionally, at-home telehealth services are currently limited. Current solutions aren't as accessible and affordable as they could be, often relying on expensive devices and protocols that not everyone can afford, or processes that are not easily adaptable o people across conditions (e.g. elderly patients, visual impairments). This is issue is compounded in rural areas, in which healthcare is imperative. Additionally, miscommunication between patient and physician due to language barriers further limits the connections between medical professionals and patients. In-person medical facilities may also be a source of infection, telemedicine reduces disease spread, making the flow of patients through healthcare more efficient.

# What it does

To mitigate this, we propose an AI powered assistant that is both affordable and highly efficient in delivering consistent, recent literature-drive, instant, and understandable initial diagnosis. We implemented this in the form of a hardware assistant (shaped like a friendly duck!) that is also affordable enough to be implemented in any home. We envision Ducktor supporting taking vitals, engaging in conversation with patients and analyzing data to provide to both patients for initial diagnosis and doctors to aid and streamline their diagnosing.

# How we built it

We collected audio input from the user via a microphone connected to an ESP32. We sent this data to one of our Flask web servers, where the PCM signals are converted into .wav audio and transcribed into text. This text is then relayed to another web server where we utilize OpenAI's technology to determine potential diagnoses from the complains of the patient, and respond with an initial diagnosis, some home remedies that may help, and a further explanation of what this means and how they should proceed with their healthcare. The information is then relayed back to the microcontroller and displayed on a screen and spoken out loud.

# Challenges

We were unable to achieve a stable WiFi connection with IEEE_5G on our ESP32, which rendered us unable to send HTTP requests to our server. This delayed the implementation of communication between our device and the cloud processing where the magic occurs, forcing us to prioritize features. We also encountered hardware issues between faulty boards and incompatibility between devices

# Accomplishments

We were able to make data sent from the device to the server secure and encrypted to ensure patient privacy throughout these exchanges. We were also able to take most of the processing to the cloud, so the device can remain affordable, small, and accessible to patients across the world.
