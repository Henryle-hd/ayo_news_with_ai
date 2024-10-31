from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()



def parse_with_groq(dom_chunks, parse_description):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    parsed_results=[]

    for i,chunk in enumerate(dom_chunks,start=1):
        print(f"Parsed batch {i} of {len(dom_chunks)}")

        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are tasked with extracting specific information: '{chunk}' .
Please follow these instructions carefully:

1. **Extract Information:** Only extract the information that directly matches the provided description: "{parse_description}".
2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.
3. **Empty Response:** If no information matches the description, return an empty string ('').
4. **Language Requirement:** Respond only in SWAHILI.

                    """
                },
                {
                    "role": "user",
                    "content": f" {parse_description}"
                },
            ],
            temperature=0.5,
            max_tokens=1024,
            top_p=0.65,
            stream=True,
            stop=None,
        )
        # result=[]
        for chunk in completion:
            # print(chunk.choices[0].delta.content or "", end="")
            # result.append()
            parsed_results.append(chunk.choices[0].delta.content or "")
        print(f"Parsed batch {i} of {len(dom_chunks)}")
    return "\n".join(parsed_results).strip()
